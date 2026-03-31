import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import scipy.sparse as sp
import os

# Create directory if it doesn't exist
if not os.path.exists('env'):
    os.makedirs('env')

# 1. Load the data (FIX: Use forward slash / to avoid path errors)
df = pd.read_csv('env/swiggy.csv') 
print(f"Initial rows loaded: {len(df)}")

# 2. Flexible Cleaning
df.columns = df.columns.str.lower().str.strip()

# Clean cost and rating
df['cost'] = df['cost'].astype(str).str.replace('₹', '').str.replace(',', '').str.strip()
df['cost'] = pd.to_numeric(df['cost'], errors='coerce')
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# Fill missing values
df['rating'] = df['rating'].fillna(df['rating'].mean())
df['cost'] = df['cost'].fillna(df['cost'].median())

# Clean text columns
df['city'] = df['city'].astype(str).str.strip()
df['cuisine'] = df['cuisine'].astype(str).str.strip()
df = df.dropna(subset=['city', 'cuisine'])

# --- OPTIMIZATION FOR MEMORY ---
# We use the top 10,000 highest-rated restaurants to make the similarity matrix 
# small enough to run on a standard computer.
df = df.sort_values(by='rating', ascending=False).head(10000).reset_index(drop=True)
print(f"Processing top 10,000 restaurants for speed and memory efficiency...")

# 3. Preprocessing & Encoding
encoder = OneHotEncoder(sparse_output=True, handle_unknown='ignore') 
encoded_vars = encoder.fit_transform(df[['city', 'cuisine']])

numerical_values = df[['rating', 'cost']].values.astype(float)
numerical_sparse = sp.csr_matrix(numerical_values)
final_encoded_matrix = sp.hstack([numerical_sparse, encoded_vars])

# 4. Calculate Similarity
# This now runs in seconds because we sampled the data
similarity = cosine_similarity(final_encoded_matrix)

# 5. Save Deliverables
sp.save_npz('encoded_data.npz', final_encoded_matrix)
with open('encoder.pkl', 'wb') as f:
    pickle.dump(encoder, f)
with open('similarity.pkl', 'wb') as f:
    pickle.dump(similarity, f)

df.to_csv('env\swiggy_cleaned_data.csv', index=False)
print("Success! All files (swiggy_cleaned_data.csv, similarity.pkl, encoder.pkl) are ready.")
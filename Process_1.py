import pandas as pd

# Load dataset
df = pd.read_csv('env/swiggy.csv')

# 1. Remove duplicates
df = df.drop_duplicates() 
# 2. Handle missing values (dropping rows with nulls for city/cuisine/rating)
df = df.dropna(subset=['city', 'cuisine', 'rating', 'cost']) 

# Save the clean version
df.to_csv('env\swiggy_cleaned_data.csv', index=False) 

import streamlit as st
import pandas as pd
import pickle

# --- PAGE CONFIG ---
st.set_page_config(page_title="Swiggy Recommender", page_icon="🍔", layout="wide")

# --- CUSTOM STYLING (Improved Headers and Spacing) ---
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #ff9933 0%, #ffffff 100%);
    }
    
    /* ENLARGED Main Title */
    .main-title {
        color: #f5f5f5; /* Swiggy Orange */
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 4rem; /* Made bigger */
        font-weight: 900;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 0px;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.1);
    }
    
    /* STYLED Subtitle */
    .sub-title {
        text-align: center; 
        color: #3d4152; 
        font-family: 'Trebuchet MS', sans-serif; /* Different font style */
        font-size: 1.5rem; /* Slightly big */
        font-weight: 500;
        margin-bottom: 40px; /* Space to push the dropdown down */
    }

    /* Restaurant Card Styling */
    .restaurant-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-bottom: 4px solid #fc8019;
        margin-bottom: 20px;
        height: 200px;
    }

    /* Button styling */
    div.stButton > button:first-child {
        background-color: #fc8019;
        color: white;
        border-radius: 20px;
        width: 100%;
        font-weight: bold;
        border: none;
        height: 3em;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATA LOADING ---
@st.cache_data
def load_data():
    # Loading the Swiggy dataset
    df = pd.read_csv('env\swiggy_cleaned_data.csv')
    return df

@st.cache_resource
def load_similarity():
    with open('similarity.pkl', 'rb') as f:
        return pickle.load(f)

df = load_data()
similarity = load_similarity()

# --- HEADER SECTION ---
st.markdown('<p class="main-title"> Swiggy Selects</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Premium recommendations for your next meal</p>', unsafe_allow_html=True)

# --- FILTERS ---
col1, col2 = st.columns(2)

with col1:
    raw_cuisines = df['cuisine'].dropna().unique()
    individual_cuisines = set()
    for item in raw_cuisines:
        parts = [c.strip() for c in str(item).split(',')]
        individual_cuisines.update(parts)
    cuisine_options = sorted(list(individual_cuisines))
    # Dropdown menu
    selected_cuisine = st.selectbox("🍜 Choose a Cuisine", cuisine_options)

with col2:
    max_val = int(df['cost'].max())
    budget = st.slider("💰 Set Max Budget (₹)", min_value=0, max_value=max_val, value=500, step=50)

# --- SEARCH ACTION ---
if st.button("🔍 Find My Next Meal"):
    # Recommendation logic based on input features like rating and cost
    cuisine_results = df[
        (df['cuisine'].str.contains(selected_cuisine, na=False, case=False)) & 
        (df['cost'] <= budget)
    ].sort_values(by='rating', ascending=False).head(4)

    if not cuisine_results.empty:
        st.subheader(f"✨ Top {selected_cuisine} in Town")
        
        cols = st.columns(len(cuisine_results))
        for i, (idx, row) in enumerate(cuisine_results.iterrows()):
            with cols[i]:
                st.markdown(f"""
                    <div class="restaurant-card">
                        <h3 style="color:#282c3f; margin-bottom:0;">{row['name']}</h3>
                        <p style="color:#fc8019; font-weight:bold;">⭐ {row['rating']}</p>
                        <p style="color:#686b78; font-size:0.9rem;">📍 {row['city']}</p>
                        <hr>
                        <p style="color:#3d4152; font-weight:700;">Cost: ₹{int(row['cost'])}</p>
                    </div>
                """, unsafe_allow_html=True)

        # Recommendation Logic using similarity measures
        top_rest_idx = cuisine_results.index[0]
        if top_rest_idx < len(similarity):
            distances = similarity[top_rest_idx]
            similar_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
            
            st.divider()
            st.subheader("🎯 People also liked these styles")
            sim_cols = st.columns(5)
            for i, match in enumerate(similar_indices):
                if match[0] in df.index:
                    r_info = df.iloc[match[0]]
                    with sim_cols[i]:
                        st.markdown(f"""
                            <div style="background-color:white; padding:10px; border-radius:10px; border-left: 5px solid #686b78;">
                                <p style="font-weight:bold; margin-bottom:0;">{r_info['name']}</p>
                                <p style="font-size:0.8rem; color:gray;">{r_info['cuisine'].split(',')[0]}</p>
                                <p style="color:#fc8019;">⭐ {r_info['rating']}</p>
                            </div>
                        """, unsafe_allow_html=True)
    else:
        st.error(f"😞 No {selected_cuisine} found under ₹{budget}!")
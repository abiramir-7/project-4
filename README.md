## 📝 Swiggy Restaurant Recommendation System
### *A Machine Learning approach to personalized food discovery*

## 📌 Project Overview
This project is a **Content-Based Recommendation System** designed to help users discover the best dining options from Swiggy's extensive restaurant data. By analyzing features like **Cuisine**, **City**, **User Ratings**, and **Cost**, the system provides tailored suggestions that match a user's specific cravings and budget.

## 🚀 Key Features
* **Smart Filtering:** Filter restaurants by individual cuisines and set a maximum budget using an interactive slider.
* **High-Resolution Recommendations:** Uses **Cosine Similarity** to suggest "Hidden Gems" that are mathematically similar to your favorite top-rated spots.
* **Swiggy-Themed UI:** A fully customized Streamlit dashboard featuring Swiggy’s signature orange palette, hover-effect cards, and a responsive layout.
* **Data Optimization:** Processed over 50,000+ rows of raw data, optimized to the top 10,000 restaurants for high-speed similarity calculations.

## 🛠️ Tech Stack
* **Language:** Python 
* **Framework:** Streamlit
  
## 📁 File Structure
* `App.py`: The main Streamlit application script.
* `Process_1.py`: Initial data cleaning and deduplication.
* `Process_2.py`: Feature engineering, One-Hot Encoding, and similarity matrix generation.
* `swiggy_cleaned_data.csv`: The final preprocessed dataset.


## ⚙️ How to Run
1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/swiggy-recommendation-system.git
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Generate the Similarity Model:**
   Run the processing script to create the necessary `.pkl` and `.npz` files:
   ```bash
   python Process_2.py
   ```
4. **Launch the App:**
   ```bash
   streamlit run App.py
   ```

## 🧠 Approach
1.  **Data Cleaning:** Handled missing ratings (filled with mean) and cleaned the "Cost" column by removing currency symbols and commas.
2.  **Encoding:** Used `OneHotEncoder` on categorical features (`City`, `Cuisine`) to convert text into a numerical format.
3.  **Similarity Matrix:** Built a feature vector for each restaurant and calculated the **Cosine Similarity** between them. 
4.  **UI/UX:** Implemented custom CSS to provide a modern, card-based interface for a premium user experience.

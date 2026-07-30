# 🍽️ Swiggy Restaurant Recommendation System

### *A Machine Learning Approach to Personalized Food Discovery*

---

## 📌 Project Overview

This project is a **Content-Based Restaurant Recommendation System** built using **Python** and **Streamlit**. It helps users discover restaurants from the Swiggy dataset based on their preferences such as **City**, **Cuisine**, **Budget**, and **Minimum Rating**.

The recommendation engine uses **One-Hot Encoding** and **Cosine Similarity** to identify restaurants that are most similar to the user's selected preferences and provides personalized recommendations through an interactive web interface.

---

## 🚀 Key Features

- 📍 **City Filter:** Search restaurants within a selected city.
- 🍜 **Cuisine Filter:** Select individual cuisines from the dataset.
- 💰 **Budget Filter:** Set a maximum budget using an interactive slider.
- ⭐ **Minimum Rating Filter:** Display only restaurants above the selected rating.
- 🤖 **Content-Based Recommendation:** Uses **Cosine Similarity** to recommend restaurants similar to the selected preferences.
- 🎨 **Interactive Streamlit Dashboard:** Clean, responsive UI with custom Swiggy-inspired styling.
- ⚡ **Optimized Processing:** The original dataset is cleaned and optimized to the top 10,000 restaurants for faster recommendation generation.

---

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** Streamlit

### Libraries Used

- **Pandas** – Data Manipulation
- **Scikit-Learn** – One-Hot Encoding & Cosine Similarity
- **SciPy** – Sparse Matrix Handling
- **Pickle** – Model Serialization

---

## 📁 Project Structure

```
Swiggy-Restaurant-Recommendation-System/
│
├── App.py
├── Process_1.py
├── Process_2.py
├── requirements.txt
├── README.md
├── swiggy.csv
└── env/
    └── swiggy_cleaned_data.csv
```

---

## ⚙️ How to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/swiggy-recommendation-system.git
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Clean the Dataset

Run the data cleaning script:

```bash
python Process_1.py
```

This creates:

- `swiggy_cleaned_data.csv`

---

### 4️⃣ Generate the Recommendation Model

Run:

```bash
python Process_2.py
```

This generates:

- `encoder.pkl`
- `similarity.pkl`
- `encoded_data.csv`
- `encoded_data.npz`

---

### 5️⃣ Launch the Streamlit Application

```bash
streamlit run App.py
```

---

## 🧠 Project Workflow

```
Raw Dataset (swiggy.csv)
            │
            ▼
      Process_1.py
(Data Cleaning & Preprocessing)
            │
            ▼
swiggy_cleaned_data.csv
            │
            ▼
      Process_2.py
(Encoding + Cosine Similarity)
            │
            ▼
Generated Model Files
            │
            ▼
         App.py
(Streamlit Dashboard)
```

---

## 🔍 Recommendation Approach

### Step 1 – Data Cleaning

- Removed duplicate records.
- Handled missing values.
- Cleaned the Cost column by removing currency symbols and commas.
- Prepared a clean dataset for preprocessing.

---

### Step 2 – Feature Engineering

Applied **One-Hot Encoding** to:

- City
- Cuisine

to convert categorical values into numerical vectors.

---

### Step 3 – Similarity Calculation

Generated feature vectors and calculated **Cosine Similarity** between restaurants to identify restaurants with similar characteristics.

---

### Step 4 – User Recommendation

Users select:

- 📍 City
- 🍜 Cuisine
- 💰 Maximum Budget
- ⭐ Minimum Rating

The application filters matching restaurants and recommends the most relevant options through the Streamlit interface.

---

## 👨‍💻 Author

**Swiggy Restaurant Recommendation System**

Machine Learning Mini Project using **Python**, **Scikit-Learn**, **Pandas**, and **Streamlit**.

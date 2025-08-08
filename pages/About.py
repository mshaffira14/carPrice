import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# ===== Plot Styling =====
from mpl_toolkits.mplot3d import Axes3D

# ===== Page Config =====
st.set_page_config(page_title="Car Dataset Overview & 3D Visualization", layout="wide")

# ===== Styling =====
st.markdown(
    """
 <style>
    body, .main, .block-container {
        background-color: #f7f9fc !important;
    }

    /* Sidebar background */
    .css-6qob1r.e1fqkh3o3 {
        background-color: #f7f9fc !important;
    }

    section[data-testid="stSidebar"] {
        box-shadow: none;
    }
    
      /* ===== Top bar / navbar ===== */
    header[data-testid="stHeader"] {
        background-color: #f7f9fc !important;
        box-shadow: none;
    }

    header[data-testid="stHeader"] > div {
        background-color: #f7f9fc !important;
    }

    /* Optional text color */
    .css-1v0mbdj, .css-1v3fvcr {
        color: #333333 !important;
    }
        .title-style {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #2685de;
            margin-bottom: 10px;
        }
        .sub-style {
            text-align: center;
            font-size: 18px;
            color: #555;
            margin-bottom: 30px;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# ===== Title =====
st.markdown(
    '<div class="title-style">🚗 Car Price Prediction: Dataset Overview</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="sub-style">Using data from <a href="https://data.mendeley.com/datasets/fmb4xmp4k5/2" target="_blank">Mendeley</a> to analyze car price prediction based on year, kilometers, and transmission type.</div>',
    unsafe_allow_html=True,
)

# ===== Load Dataset =====
df = pd.read_csv("data/car_dataset.csv")

# ===== Dataset Overview =====
with st.container():
    st.markdown("### 📄 Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)
    st.markdown(
        """
    **About this dataset:**

    This dataset is designed for building machine learning models to predict the price of used cars based on features like:

    - 🚙 **Transmission** (`0 = Manual`, `1 = Automatic`)
    - ⛽ **Fuel type**
    - 📅 **Model year**
    - 📏 **Engine capacity**
    - 📉 **Kilometers driven**
    - 💰 **Selling price**

    📌 **Source**: [Mendeley Dataset](https://data.mendeley.com/datasets/fmb4xmp4k5/2)
    """
    )

# ===== 3D Visualization =====
st.markdown("### 📈 3D Visualization: Price vs Year vs KM by Transmission")

df["transmission"] = df["transmission"].astype(str)
manual = df[df["transmission"].str.contains("0")].copy()
automatic = df[df["transmission"].str.contains("1")].copy()

fig = plt.figure(figsize=(20, 10))

# View 1
ax1 = fig.add_subplot(131, projection="3d")
ax1.scatter(
    manual["price"], manual["model_year"], manual["kilometers_run"], color="skyblue"
)
ax1.scatter(
    automatic["price"],
    automatic["model_year"],
    automatic["kilometers_run"],
    color="orange",
)
ax1.set_xlabel("Selling Price")
ax1.set_ylabel("Model Year")
ax1.set_zlabel("KM Driven")
ax1.set_title("View 1: Price vs Year vs KM")
ax1.legend(["Manual", "Automatic"])

# View 2
ax2 = fig.add_subplot(132, projection="3d")
ax2.scatter(
    manual["kilometers_run"], manual["price"], manual["model_year"], color="skyblue"
)
ax2.scatter(
    automatic["kilometers_run"],
    automatic["price"],
    automatic["model_year"],
    color="orange",
)
ax2.set_xlabel("KM Driven")
ax2.set_ylabel("Selling Price")
ax2.set_zlabel("Model Year")
ax2.set_title("View 2: KM vs Price vs Year")
ax2.legend(["Manual", "Automatic"])

# View 3
ax3 = fig.add_subplot(133, projection="3d")
ax3.scatter(
    manual["model_year"], manual["price"], manual["kilometers_run"], color="skyblue"
)
ax3.scatter(
    automatic["model_year"],
    automatic["price"],
    automatic["kilometers_run"],
    color="orange",
)
ax3.set_xlabel("Model Year")
ax3.set_ylabel("Selling Price")
ax3.set_zlabel("KM Driven")
ax3.set_title("View 3: Year vs Price vs KM")
ax3.legend(["Manual", "Automatic"])

st.pyplot(fig)

# ===== Preprocessing Explanation =====
st.markdown("### 🧹 Data Preprocessing & Feature Engineering")

st.markdown(
    """
**1. Data Cleaning:**
- Removed noisy column `car_name` with 1100+ unique values.
- Dropped rows with missing or rare entries in `body_type` and `fuel_type`.
- Mapped multiple `fuel_type` values into 4 clean categories: `Oil`, `CNG and Oil`, `Hybrid`, `LPG and Oil`.

**2. Outlier Detection:**
- Used **Tukey's Method** to remove price & mileage outliers.

**Example:** Price distribution before and after cleaning:
"""
)

# Plot price distribution before & after
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
axes[0].hist(df["price"], bins=50, color="red", edgecolor="black")
axes[0].set_title("Before Cleaning")
axes[1].hist(
    df[df["price"] < 75_00_000]["price"], bins=50, color="green", edgecolor="black"
)
axes[1].set_title("After Cleaning")
st.pyplot(fig)

# ===== Encoding =====
st.markdown(
    """
**3. Encoding:**
- Applied **Label Encoding** on high-cardinality features like `brand`, `car_model`.
- Applied **One-Hot Encoding** on `transmission` and `fuel_type`.

```python
encoded_df = pd.get_dummies(df[["transmission", "fuel_type"]])
"""
)

st.dataframe(pd.get_dummies(df[["transmission", "fuel_type"]]).head())

# ===== Scaling =====
st.markdown("4. Feature Scaling using Min-Max Scaler:")
st.latex(r"X_{\text{scaled}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}")

scaled_df = df[["engine_capacity", "kilometers_run"]].copy()
scaler = MinMaxScaler()
scaled_df[["engine_capacity", "kilometers_run"]] = scaler.fit_transform(scaled_df)

st.markdown("Below is the result of scaled numerical features:")
st.dataframe(scaled_df.head())

# ===== Modeling Results =====
st.markdown("### 🧠 Model Performance Comparison")

r2_scores = [70.55, 70.55, 86.99, 89.99, 92.12]
models = ["Linear", "LASSO", "Decision Tree", "Random Forest", "XGBoost"]

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(models, r2_scores, color="teal")
ax.set_ylabel("R² Score (%)")
ax.set_title("Performance Comparison of ML Models")
st.pyplot(fig)

st.markdown(
    """
📌 Summary:

📈 Best Model: XGBoost, with R² = 92.12%

✅ Tuned using GridSearchCV

📊 Evaluation metrics: R², RMSE, MAE

This predictive model is deployable and can assist buyers in evaluating fair prices for used cars.
"""
)

st.sidebar.markdown(
    """
    <div style="
        background-color: #cce5ff;
        padding: 12px;
        border-radius: 8px;
        border-left: 6px solid #339af0;
        color: #084298;
        font-weight: 500;
        font-size: 16px;
        margin-bottom: 1rem;">
        📘 Choose a page above.
    </div>
    """,
    unsafe_allow_html=True,
)

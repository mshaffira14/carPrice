import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objects as go

# Page config
st.set_page_config(page_title="Car Dataset Overview & 3D Visualization", layout="wide")

# ======= Styling =======
st.markdown(
    """
    <style>
        .main {
            background-color: #f7f9fc;
        }
        .title-style {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #2E8B57;
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

# ======= Title & About =======
st.markdown(
    '<div class="title-style">🚗 Car Price Prediction: Dataset Overview</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="sub-style">Using data from <a href="https://data.mendeley.com/datasets/fmb4xmp4k5/2" target="_blank">Mendeley</a> to analyze car price prediction based on year, kilometers, and transmission type.</div>',
    unsafe_allow_html=True,
)

# ======= Load Dataset =======
df = pd.read_csv("car_dataset.csv")

# ======= Dataset Overview =======
with st.container():
    st.markdown('<div class="box">', unsafe_allow_html=True)
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
    st.markdown("</div>", unsafe_allow_html=True)

# ======= 3D Visualization =======
st.markdown('<div class="box">', unsafe_allow_html=True)
st.markdown("### 📈 3D Visualization: Price vs Year vs KM by Transmission")

# Data Filtering
df["transmission"] = df["transmission"].astype(str)
manual = df[df["transmission"].str.contains("0")].copy()
automatic = df[df["transmission"].str.contains("1")].copy()

# Matplotlib 3D Plot
fig = plt.figure(figsize=(20, 10))

# View 1
ax1 = fig.add_axes([0.05, 0.5, 0.3, 0.4], projection="3d")
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
ax2 = fig.add_axes([0.38, 0.5, 0.3, 0.4], projection="3d")
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
ax3 = fig.add_axes([0.71, 0.5, 0.3, 0.4], projection="3d")
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
st.markdown("</div>", unsafe_allow_html=True)

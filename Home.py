import streamlit as st
from predictor import get_price

st.markdown(
    """
    <style>
     .main {
            background-color: #f7f9fc;
        }
        .header-container {
            background-image: url('https://images.unsplash.com/photo-1630369281377-839f10973a72?q=80&w=1170&auto=format&fit=crop');
            background-size: cover;
            background-position: center;
            padding: 100px 0 80px 0;
            text-align: center;
            color: white;
            border-radius: 20px;
            overflow: hidden;
            margin-bottom: 20px;
        }

        .header-container h1 {
            font-size: 60px;
            margin: 0;
            margin-top: -30px; 
            color: white;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
        }

        .header-container p {
            font-size: 24px;
            margin-top: 10px;
            margin-bottom: 30px;
            color: white;
            text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.7);
        }

        .form-container {
            padding: 30px;
            border-radius: 10px;
            color: white;
            margin-top: 30px;
        }

        .stSelectbox > div, .stTextInput > div, .stNumberInput > div {
            background-color: white;
            color: black;
            border-radius: 5px;
        }

        .stButton button {
            background-color: #d6ff00;
            color: black;
            font-weight: bold;
            padding: 0.75em 2em;
            border: none;
            border-radius: 5px;
        }

        .stButton button:hover {
            background-color: #bada00;
        }

        .scroll-button {
            margin-top: 20px;
            display: inline-block;
            padding: 12px 25px;
            font-size: 16px;
            background-color: #d6ff00;
            color: black;
            font-weight: bold;
            border: none;
            border-radius: 5px;
            text-decoration: none;
        }

        .scroll-button:hover {
            background-color: #bada00;
            color: black;
        }

        .center-title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 20px;
        }
    </style>

    <div class="header-container">
        <h1>MOST-RELIABLE PRICE</h1>
        <p>Sell your car at a best price</p>
        <a href="#form-prediksi" class="scroll-button">Predict Your Car</a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Form Input
st.markdown('<div id="form-prediksi" class="form-container">', unsafe_allow_html=True)

# Judul
st.markdown(
    '<div class="center-title">Used Car Price Predictions</div>', unsafe_allow_html=True
)

# Kolom input
col1, col2 = st.columns(2)
with col1:
    transmission = st.selectbox("Transmission", ["0 (Manual)", "1 (Automatic)"])
    brand = st.text_input("Make (Merek)", "Toyota")
    model_year = st.number_input(
        "Tahun Mobil", min_value=1980, max_value=2025, value=2009
    )
    engine_capacity = st.number_input(
        "Kapasitas Mesin (cc)", min_value=500, max_value=5000, value=1500
    )

with col2:
    fuel_type = st.selectbox(
        "Fuel Type", ["OIL", "HYBRID", "LPG and OIL", "CNG and OIL"]
    )
    model = st.text_input("Model", "Allion")
    body_type = st.selectbox(
        "Tipe Body", ["Saloon", "SUV", "Hatchback", "Station Wagon"]
    )
    kilometers_run = st.number_input("Jarak Tempuh (km)", min_value=0, value=60000)

col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    if st.button("Price Prediction"):
        harga = get_price(
            transmission,
            fuel_type,
            brand,
            model,
            model_year,
            body_type,
            engine_capacity,
            kilometers_run,
        )
        st.success(f"💰 Estimated Car Price: ${harga:,.2f}")

st.markdown("</div>", unsafe_allow_html=True)

st.sidebar.success("Choose a page above.")

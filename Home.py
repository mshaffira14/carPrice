import streamlit as st
from predictor import get_price

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
            background-color: #b5f3f5;
            color: black;
            font-weight: bold;
            padding: 0.75em 2em;
            border: none;
            border-radius: 5px;
        }

        .stButton button:hover {
            background-color: #50e5eb;
            color: black;
        }
        
        .stButton button:focus,
        .stButton button:active,
        .stButton button:visited {
            color: black !important;
            outline: none !important;
            box-shadow: none !important;
        }

        .scroll-button {
            margin-top: 20px;
            display: inline-block;
            padding: 12px 25px;
            font-size: 16px;
            background-color: #b5f3f5;
            color: black;
            font-weight: bold;
            border: none;
            border-radius: 5px;
            text-decoration: none;
        }

        .scroll-button:hover {
            background-color: #50e5eb;
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

col_btn1, col_btn2, col_btn3 = st.columns([2, 1, 1])
with col_btn1:
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
        st.markdown(
            f"""
    <div style="
        background-color: #50e5eb;
        padding: 16px;
        border-radius: 8px;
        border-left: 6px solid #339af0;
        color: #084298;
        font-weight: 500;
        font-size: 18px;">
        💰 Estimated Car Price: <strong>${harga:,.2f}</strong>
    </div>
    """,
            unsafe_allow_html=True,
        )

st.markdown("</div>", unsafe_allow_html=True)

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

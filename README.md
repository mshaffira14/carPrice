# 🚗 Used Car Price Prediction App

A Streamlit web application to predict the price of used cars based on several key input features.

## 📌 Features

- Predicts **used car prices** based on input data:
  - Transmission (Manual / Automatic)
  - Fuel Type (OIL, HYBRID, LPG and OIL, CNG and OIL)
  - Make (Car Brand)
  - Model
  - Model Year
  - Body Type
  - Engine Capacity (cc)
  - Kilometers Run
- Clean and user-friendly UI built with **Streamlit**
- Model powered by **XGBoost Regressor**
- Preprocessing handled with **MinMaxScaler**

## 🚀 How to Run Locally

1. Clone this repository:

   ```bash
   git clone https://github.com/mshaffira14/carPrice.git
   cd carPrice

2. Install dependencies:
    ```bash
   pip install -r requirements.txt
   
4. Run the app:
    ```bash
   streamlit run Home.py

## 📁 Project Structure
 ```bash
carPrice/
│
├── data/                      # Contains dataset
│   └── car_dataset.csv
│
├── models/                    # Contains trained model and scaler
│   ├── xg_boost_model.json
│   └── min_max_scaler.save
│
├── pages/                     # Other Streamlit pages
│   └── About.py
│
├── Home.py                    # Main Streamlit app page
├── predictor.py               # Prediction logic
├── requirements.txt
└── README.md

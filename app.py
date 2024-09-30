import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the saved model
with open('model_pickle', 'rb') as f:
    model = pickle.load(f)

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #f4f4f4;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background-image: linear-gradient(to bottom, #ffffff, #d7e1ec);
        padding: 20px;
        border-radius: 15px;
    }
    .header {
        background-color: #2980b9;
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
    .title {
        color: #2c3e50;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
        padding: 20px;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
    }
    .stFileUploader {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Header and description
st.markdown("<div class='header'><h2>Flood Prediction App</h2></div>", unsafe_allow_html=True)
st.markdown("<h4 class='title'>Choose an option to predict floods based on the provided data.</h4>", unsafe_allow_html=True)

# Option selection
option = st.selectbox(
    "Choose an option",
    ["Predict based on factors", "Predict based on rainfall"]
)

if option == "Predict based on factors":
    st.subheader("Enter the factors:")
    feature_columns = [
    'MonsoonIntensity', 'TopographyDrainage', 'RiverManagement', 'Deforestation', 'Urbanization',
    'ClimateChange', 'DamsQuality', 'Siltation', 'AgriculturalPractices',
    'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'
]
    
    # Collect user inputs
    inputs = {col: st.slider(f"{col}", min_value=1, max_value=10) for col in feature_columns}
    
    # Create a DataFrame for prediction
    user_data = pd.DataFrame([inputs], columns=feature_columns)
    
    if st.button('Predict'):
        # Make prediction
        y_pred_proba = model.predict_proba(user_data)[:, 1]
        y_pred = (y_pred_proba > 0.5).astype(int)
        result = 'YES' if y_pred[0] == 1 else 'NO'
        
        st.write(f"Prediction: {result}")
        
        # Optionally display model accuracy
        # accuracy = accuracy_score(y_test, model.predict(X_test))
        # st.write(f"Model Accuracy: {accuracy:.2f}")

elif option == "Predict based on rainfall":
    st.subheader("Enter the monthly rainfall data:")
    months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    
    rainfall_data = []
    for month in months:
        rainfall = st.slider(f"Rainfall for {month} (0-1000)", min_value=0, max_value=1000)
        rainfall_data.append(rainfall)
    
    if st.button('Predict'):
        annual_rainfall = sum(rainfall_data)
        flood_prediction = 'YES' if annual_rainfall > 3000 else 'NO'
        st.write(f"Flood prediction based on annual rainfall: {flood_prediction}")

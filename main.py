import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from PIL import Image


model = tf.keras.models.load_model('flood_classifier_model.h5')


st.markdown("""
    <style>
    body {
        background-image: url('BG.jpeg'); 
        background-size: cover; 
        background-position: center; 
        background-attachment: fixed; 
        background-repeat: no-repeat; 
    }
    .stApp {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 20px;
        border-radius: 15px;
    }
    .title {
        color: #2c3e50;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
        padding: 20px;
    }
    .header {
        background-color: #2980b9;
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
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

st.markdown("<div class='header'><h2>Flood Detection App</h2></div>", unsafe_allow_html=True)
st.markdown("<h4 class='title'>Upload an image to predict if it's a flood or not.</h4>", unsafe_allow_html=True)


uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    st.write("Classifying...")
    img = image.resize((150, 150))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    
    prediction = model.predict(img_array)
    result = 'Flood' if prediction[0] < 0.5 else 'No Flood'
    
    st.markdown(f"<h3 style='text-align: center; color: #2980b9;'>{result}</h3>", unsafe_allow_html=True)


st.markdown("<hr style='margin-top: 50px;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>© 2024 Flood Detection App | Built with Streamlit</p>", unsafe_allow_html=True)

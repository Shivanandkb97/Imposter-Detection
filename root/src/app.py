import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Load your pre-trained model
model = load_model('NuAA_model2.h5')  # Replace 'your_model.h5' with your model file path

def preprocess_image(image):
    """Preprocess the image for model prediction."""
    img_resized = cv2.resize(np.array(image), (128, 128))  # Resize to match model input
    img_normalized = img_resized / 255.0  # Normalize pixel values
    img_expanded = np.expand_dims(img_normalized, axis=0)  # Add batch dimension
    return img_expanded

def classify_image(image):
    """Classify the image using the trained model."""
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    return 'Real' if prediction[0] > 0.5 else 'Fake'

# Streamlit UI
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
        }
        .title {
            text-align: center;
            font-size: 40px;
            color: #4CAF50;
            margin-top: 20px;
            font-weight: bold;
        }
        .description {
            text-align: center;
            font-size: 20px;
            margin-bottom: 30px;
            color: #333;
        }
        .option {
            text-align: center;
            font-size: 20px;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .upload-container, .capture-container {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            margin-top: 20px;
            padding: 20px;
            border-radius: 10px;
            background-color: #ffffff;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
            transition: 0.3s;
        }
        .upload-container:hover, .capture-container:hover {
            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Imposter Detection</div>', unsafe_allow_html=True)
st.markdown('<div class="description">We used Fake Net Model to predict the images</div>', unsafe_allow_html=True)

# Create buttons for selecting the action
option = st.radio("", ("Upload Photo", "Take Photo"), index=0)

if option == "Upload Photo":
    st.markdown('<div class="upload-container">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption='Uploaded Image', use_column_width=True)

        result = classify_image(img)
        st.write(f"Prediction: {result}")

    st.markdown('</div>', unsafe_allow_html=True)

elif option == "Take Photo":
    st.markdown('<div class="capture-container">', unsafe_allow_html=True)
    img_file_buffer = st.camera_input("Take a picture")

    if img_file_buffer is not None:
        img = Image.open(img_file_buffer)
        st.image(img, caption='Captured Image', use_column_width=True)

        result = classify_image(img)
        st.write(f"Prediction: {result}")

    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.write("Please upload an image or take a picture.")

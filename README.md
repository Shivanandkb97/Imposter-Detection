# Imposter Detection System

## Overview

The **Imposter Detection System** is an advanced deep learning solution designed to identify fraudulent activities and unauthorized access with high accuracy. By leveraging state-of-the-art algorithms and custom datasets, the system effectively analyzes patterns and behaviors to detect imposters in real-time.

## Key Features

- **Real-time Detection**: Identifies imposters as they attempt unauthorized access or fraudulent activities.
- **Streamlit-based Interface**: User-friendly front-end built with Streamlit for easy interaction and visualization.
- **Advanced Deep Learning Models**: Utilizes custom-built deep learning models, trained on comprehensive datasets.
- **Custom Datasets**: Includes datasets like NUAA and Yonsei University for robust training and validation.
- **High Accuracy**: Optimized algorithms ensure precise and reliable detection outcomes.
- **Behavioral Analysis**: Detects anomalies through in-depth pattern and behavior analysis.


## Front-End and Application Flow

The system includes a **Streamlit-based web application** that serves as the front-end for users to interact with the model. The core application logic is handled in the `app.py` file, which:
1. Provides an intuitive interface for uploading image files.
2. Displays results in real-time after processing inputs through the model.
3. Offers visualization of detected patterns or anomalies.

## Datasets

The project uses both publicly available datasets and custom-built datasets for training and evaluation:
- **NUAA Dataset**: A facial dataset for spoof detection.
- **Yonsei University Dataset**: Real and fake face datasets for deep learning.

**Some dataset examples**:

![collecting-dataset](https://github.com/user-attachments/assets/de7e81f8-7e56-4fb0-a8bd-2c352bce5661)


## Methodology

1. **Data Collection**: Data is gathered from multiple sources to create a diverse and balanced dataset.
2. **Preprocessing**: Data is cleaned, resized, and normalized for model compatibility.
3. **Model Training**: The system uses advanced neural networks, including a custom-built **Fake Net Model**, to train for imposter detection.
4. **Evaluation**: The models are rigorously evaluated using accuracy, precision, and recall metrics.
5. **Deployment**: The trained model is deployed for real-time imposter detection.

## Flow Diagram

![graphviz (7)](https://github.com/user-attachments/assets/6bf05dbb-b9c0-4a11-b15f-0427e8b72b04)


## Technologies Used

- **Deep Learning Frameworks**: TensorFlow, Keras
- **Programming Languages**: Python
- **Development Tools**: Google Colab
- **Data Handling**: Numpy, Pandas
- **Visualization**: Matplotlib, Seaborn

## How It Works

1. Upload an image for analysis.
2. The system analyzes the input using trained deep learning models.
3. A real-time decision is made, categorizing the input as **Genuine** or **Imposter**.

### Workflow of Imposter Detection System

1. **Data Collection**  
   Collect images and videos from datasets like NUAA, Yonsei, and Forensic++.

2. **Data Preprocessing**  
   Clean, resize, and normalize data to prepare it for model training.

3. **Model Training**  
   Train the deep learning models (e.g., Fake Net Model) on preprocessed data.

4. **Model Evaluation**  
   Evaluate the model using metrics like accuracy, precision, and recall.

5. **Deployment**  
   Deploy the trained model to the Streamlit-based web application.

6. **Real-Time Results**  
   Process user inputs (images) and classify them as **Genuine** or **Imposter**.


![image](https://github.com/user-attachments/assets/35b98541-ff07-441f-abc0-e560b14cc7eb)

### Results

**Classification Report**

![WhatsApp Image 2024-12-10 at 23 21 06_0c7fd892](https://github.com/user-attachments/assets/962d018a-3d66-40aa-b3aa-76469a415ed8)


**Confusion Matrix**

![WhatsApp Image 2024-12-10 at 23 18 10_f2d1e19a](https://github.com/user-attachments/assets/7bed4317-e67f-4ffd-926d-35e9f6445fe2)

**ROC Curve**

![WhatsApp Image 2024-12-10 at 23 19 18_24eb4c7f](https://github.com/user-attachments/assets/45c80b5a-8145-4785-ac29-125bdf17a05f)

**AUC Curve**

![WhatsApp Image 2024-12-10 at 23 19 19_c6ffd0af](https://github.com/user-attachments/assets/679fab03-a31a-4287-b40f-a986a20fb981)

**Model Accuracy**

![WhatsApp Image 2024-12-10 at 23 19 19_3e6f6c06](https://github.com/user-attachments/assets/4dc68196-fbb6-47fb-9b9d-e4a6918cb54d)


**Model Loss**

![WhatsApp Image 2024-12-10 at 23 19 20_45acede2](https://github.com/user-attachments/assets/dd587173-4394-44f9-a476-41120951aa42)


## Challenges

- **Complex Image Recognition**: Identifying imposters in images with varying quality and lighting.
- **Dataset Variability**: Ensuring the system works with diverse datasets and scenarios.
- **Real-Time Processing**: Balancing accuracy with processing speed.

## Future Enhancements

- **Integration with Security Systems**: Extend the system to integrate seamlessly with access control and surveillance systems.
- **Behavioral Analysis Expansion**: Incorporate more behavioral cues for enhanced detection.
- **Scalability**: Optimize the system for deployment on large-scale applications.


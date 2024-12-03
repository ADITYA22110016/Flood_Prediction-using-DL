# Flood_Prediction Using Dl
# Flood Prediction System

This repository contains the implementation of a hybrid flood prediction system that integrates **image classification** and **statistical modeling** to provide accurate flood risk assessments. Developed using **Streamlit**, the system offers an intuitive and interactive user interface, making it accessible to a wide range of users. 

## Overview

The flood prediction system leverages diverse data inputs, including images and statistical parameters, to calculate flood probabilities. It is designed to consider both static and dynamic flood risk factors, integrating them into a **weighted probability mechanism** for final decision-making.

### Flowchart Reference
The flowchart (Fig. 2) in report  illustrates the comprehensive architecture of the system, detailing the interaction between image classification and statistical modeling.

---

## Features

### 1. **Image Classification**
- **Land Cover Classification**: Users upload images representing specific land cover types (e.g., deforestation, paddy fields, or construction zones). 
  - Implications of land cover types:
    - **Deforestation**: Increased runoff and flood risk.
    - **Paddy Fields**: Partial mitigation due to water retention capacity.
    - **Construction Areas**: Reduced natural drainage, increasing flood risk.
  - The model assigns flood probabilities to each land cover type based on training with labeled datasets.

- **Rainfall Intensity Classification**: Users upload images indicating rainfall intensity.
  - Categories: Light, Moderate, Heavy.
  - The model classifies images and assigns probabilities based on rainfall intensity's impact on flood risks.

The combined probabilities from these models contribute real-time insights into the final prediction.

---

### 2. **Statistical Modeling**
- **Input Parameters**:
  - Geospatial: Latitude, Longitude, Elevation (m).
  - Meteorological: Rainfall (mm), Temperature (°C), Humidity (%), River Discharge (m³/s), Water Level (m).
  - Land Use: Land Cover Type, Soil Type, Population Density, Infrastructure, Historical Flood Occurrences.
- **Model Analysis**:
  - Identifies patterns in data to predict flood probabilities.
  - Provides comprehensive insights using historical datasets.
  - Assigned the highest weight (90%) in final probability calculations.

---

### 3. **Flood Probability Calculation**
The final flood probability is calculated using the following weighted sum formula:

**PFlood = W1 × PLandcover + W2 × PRainfallintensity + W3 × PStatisticalModel**

Where:
- **PFlood**: Final flood probability.
- **PLandCover**: Probability from land cover classification.
- **PRainfallintensity**: Probability from rainfall intensity classification.
- **PStatisticalModel**: Probability from statistical modeling.
- **W1, W2, W3**: Weights assigned to each model.
  - **W1 = W2 = 0.05**
  - **W3 = 0.90**

---

## Advantages
- **Holistic Approach**: Combines real-time image analysis with comprehensive statistical modeling.
- **User-Friendly Interface**: Built with Streamlit for easy interaction.
- **Dynamic and Scalable**:
  - Real-time environmental insights (e.g., deforestation, heavy rainfall).
  - Modular design allows integration of additional data sources like remote sensing or IoT-based measurements.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/abhijeet8080/Flood_Prediction_2
Navigate to the project directory:
bash
Copy code
cd Flood_Prediction_2
Install required dependencies:
bash
Copy code
pip install -r requirements.txt
Run the Streamlit application:
bash
Copy code
streamlit run app.py
Usage
Upload Images:
Upload an image of land cover (e.g., deforestation, paddy fields).
Upload an image of rainfall intensity.
Enter Statistical Data:
Provide parameters such as rainfall, temperature, humidity, elevation, etc.
View Predictions:
The system calculates the final flood probability using the weighted mechanism and displays results in real time.
Future Enhancements
Integration of remote sensing imagery.
IoT-based real-time environmental measurements.
Expansion of datasets for improved accuracy.


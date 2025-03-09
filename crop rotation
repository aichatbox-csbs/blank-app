import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
from sklearn.preprocessing import StandardScaler

# Load the trained models and encoders (Assuming these are saved already)
# with open('model.pkl', 'rb') as f:
#     model = pickle.load(f)

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv('Crop_recommendation.csv')
    return df

df = load_data()

# Crop Rotation Data
crop_rotation_map = {
    'rice': ['lentil', 'chickpea', 'mustard'],
    'maize': ['soybean', 'blackgram', 'pea'],
    'wheat': ['mustard', 'pea', 'sunflower'],
    'cotton': ['groundnut', 'pigeon peas', 'jowar'],
    'sugarcane': ['barley', 'lentil', 'green gram'],
    'carrot': ['onion', 'beetroot', 'radish'],
    'beetroot': ['cabbage', 'cauliflower', 'garlic'],
    'watermelon': ['pumpkin', 'tomato', 'cucumber'],
    'tomato': ['beans', 'cabbage', 'coriander'],
    'onion': ['tomato', 'carrot', 'potato'],
    'garlic': ['peas', 'mustard', 'lentil'],
    'cabbage': ['tomato', 'carrot', 'radish'],
    'cauliflower': ['onion', 'spinach', 'lettuce'],
    'pumpkin': ['beans', 'okra', 'peas'],
    'chickpea': ['maize', 'millet', 'sorghum'],
    'blackgram': ['rice', 'maize', 'sesame'],
    'lentil': ['rice', 'mustard', 'cotton'],
    'pigeon peas': ['groundnut', 'pearl millet'],
    'soybean': ['maize', 'barley', 'jowar'],
    'mustard': ['wheat', 'barley', 'green gram'],
    'groundnut': ['pigeon peas', 'castor', 'sunflower'],
    'peas': ['carrot', 'potato', 'cabbage'],
    'potato': ['wheat', 'maize', 'mustard'],
    'sunflower': ['mustard', 'wheat', 'barley'],
    'mango': ['legumes', 'turmeric', 'ginger'],
    'banana': ['legumes', 'coconut', 'pineapple'],
    'apple': ['walnut', 'pear', 'cherry'],
    'grapes': ['citrus', 'olive', 'pomegranate'],
    'papaya': ['banana', 'mango', 'coconut'],
    'coconut': ['pineapple', 'banana', 'mango'],
    'coffee': ['tea', 'cardamom', 'black pepper'],
    'tea': ['coffee', 'black pepper', 'ginger'],
    'cashew': ['mango', 'coconut', 'banana'],
    'pomegranate': ['grapes', 'guava', 'citrus'],
    'guava': ['pomegranate', 'papaya', 'lemon'],
    'orange': ['lemon', 'grapefruit', 'pomegranate'],
    'lemon': ['orange', 'papaya', 'coconut'],
    'jackfruit': ['banana', 'coconut', 'areca nut'],
    'areca nut': ['black pepper', 'coffee', 'cardamom'],
    'black pepper': ['coffee', 'coconut', 'areca nut'],
    'muskmelon': ['pumpkin', 'cucumber', 'okra'],
    'mothbeans': ['millet', 'sorghum', 'green gram'],
    'mungbean': ['maize', 'pigeon peas', 'sesame']    
}

def get_crop_info(crop):
    return f"Information about {crop}: This crop requires specific care and conditions. Proper soil, water, and climate management are crucial."

def get_soil_health_tips(crop):
    return f"Soil Health Tips for {crop}: Use organic compost, crop rotation, and green manure to enhance fertility. Avoid excessive chemical fertilizers."

def get_water_management_tips(crop):
    return f"Water Management Tips for {crop}: Implement drip irrigation, rainwater harvesting, and mulching to conserve moisture and prevent overwatering."

st.title("🌾 Smart Agriculture Advisory System")
st.sidebar.image("https://www.example.com/agriculture-theme.jpg", use_column_width=True)
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Select an Option", ["Select Crop", "Crop Rotation Strategy", "Soil Health", "Water Management Techniques", "Past History"])

if option == "Select Crop":
    crop = st.selectbox("Choose a Crop", df['label'].unique())
    st.write(get_crop_info(crop))
    
elif option == "Crop Rotation Strategy":
    crop = st.selectbox("Choose a Crop", df['label'].unique())
    rotation = crop_rotation_map.get(crop, ["No rotation data available"])
    st.write(f"Best Crop Rotation for {crop}: {', '.join(rotation)}")
    
elif option == "Soil Health":
    crop = st.selectbox("Choose a Crop", df['label'].unique())
    st.write(get_soil_health_tips(crop))
    
elif option == "Water Management Techniques":
    crop = st.selectbox("Choose a Crop", df['label'].unique())
    st.write(get_water_management_tips(crop))
    
elif option == "Past History":
    st.write("Past records of selected crops")
    st.table(df.head(20))

st.sidebar.write("🚜 Built for farmers to enhance crop production and sustainability.")

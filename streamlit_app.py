import streamlit as st
import pandas as pd

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
    'mango': ['citrus', 'banana', 'papaya'],
    'banana': ['legumes', 'coconut', 'pineapple'],
    'apple': ['walnut', 'pear', 'cherry'],
    'grapes': ['citrus', 'olive', 'pomegranate'],
    'papaya': ['banana', 'mango', 'coconut'],
    'coconut': ['pineapple', 'banana', 'mango'],
    'coffee': ['tea', 'cardamom', 'black pepper'],
    'tea': ['coffee', 'black pepper', 'ginger'],
    'muskmelon': ['pumpkin', 'cucumber', 'okra'],
    'mothbeans': ['millet', 'sorghum', 'green gram'],
    'mungbean': ['maize', 'pigeon peas', 'sesame']
}


# Sidebar User Input
st.sidebar.title("Crop Selection")
selected_crop = st.sidebar.selectbox("Select a Crop", list(crop_rotation_map.keys()))

# Display Recommended Crop Rotation
st.subheader(f"Recommended Crop Rotation for {selected_crop}")
st.write("Rotate your crop with:", ", ".join(crop_rotation_map[selected_crop]))

# Input Parameters for Crop Suitability
st.subheader("Enter Soil Parameters")
humidity = st.slider("Humidity (%)", 0, 100, 50)
rainfall = st.slider("Rainfall (mm)", 0, 500, 100)
ph = st.slider("Soil pH", 4.0, 9.0, 6.5)

# Display Data Table (Mock Data)
st.subheader("Crop Data Table")
df = pd.DataFrame({
    "Crop": list(crop_rotation_map.keys()),
    "Recommended Rotation": [", ".join(v) for v in crop_rotation_map.values()]
})
st.dataframe(df)

# Heatmap Visualization (Mock Data)
st.subheader("Feature Correlation Heatmap")
mock_data = pd.DataFrame({
    "Humidity": [humidity] * len(df),
    "Rainfall": [rainfall] * len(df),
    "PH": [ph] * len(df),
})

fig, ax = plt.subplots()
sns.heatmap(mock_data.corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)




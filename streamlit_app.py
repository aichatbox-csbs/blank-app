import streamlit as st
import pandas as pd
import numpy as np
# Load the trained model
model = joblib.load("crop_recommendation.csv")  # Ensure the model is availabl

# Crop cultivation steps
crop_steps = {
    "Rice": "1. Prepare land with good water retention.\n2. Use quality seeds.\n3. Irrigate frequently.\n4. Apply fertilizers and pest control.",
    "Wheat": "1. Plow land properly.\n2. Sow seeds in cool temperatures.\n3. Use nitrogen-rich fertilizers.\n4. Harvest when golden brown."
}

# UI Layout
st.title("Smart Crop Advisor for Farmers")
st.sidebar.header("Select Options")
option = st.sidebar.selectbox("Choose an Action", ["Select a Crop", "Predict Crop", "Soil Health Analysis", "Past Cultivation Histories"])

if option == "Select a Crop":
    st.subheader("Choose a Crop for Guidance")
    crop_choice = st.selectbox("Select a Crop", list(crop_steps.keys()))
    st.write(f"### Steps to cultivate {crop_choice}:")
    st.write(crop_steps[crop_choice])
    image = get_crop_image(crop_choice)
    if image:
        st.image(image, caption=crop_choice, use_column_width=True)

elif option == "Predict Crop":
    st.subheader("Enter Soil Parameters to Predict the Best Crop")
    N = st.number_input("Nitrogen", min_value=0, max_value=200, value=50)
    P = st.number_input("Phosphorus", min_value=0, max_value=200, value=50)
    K = st.number_input("Potassium", min_value=0, max_value=200, value=50)
    PH = st.number_input("pH Level", min_value=0.0, max_value=14.0, value=6.5)
    Rainfall = st.number_input("Rainfall (mm)", min_value=0, max_value=1000, value=200)
    Humidity = st.number_input("Humidity (%)", min_value=0, max_value=100, value=50)
    
    if st.button("Predict Crop"):
        input_data = np.array([[Humidity, Rainfall, PH, N, P, K]])
        predicted_crop = model.predict(input_data)[0]
        st.success(f"Recommended Crop: {predicted_crop}")
        image = get_crop_image(predicted_crop)
        if image:
            st.image(image, caption=predicted_crop, use_column_width=True)

elif option == "Soil Health Analysis":
    st.subheader("Check Your Soil Health")
    ph_level = st.slider("Soil pH Level", 0.0, 14.0, 6.5)
    if ph_level < 5.5:
        st.warning("Your soil is too acidic. Consider adding lime.")
    elif ph_level > 7.5:
        st.warning("Your soil is too alkaline. Add organic matter to balance.")
    else:
        st.success("Your soil is healthy!")

elif option == "Past Cultivation Histories":
    st.subheader("View Past Cultivation Records")
    past_data = pd.read_csv("past_crop_data.csv")  # Assume this CSV contains past records
    st.dataframe(past_data)

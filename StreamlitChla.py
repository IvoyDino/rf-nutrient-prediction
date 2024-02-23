# Streamlit app script (StreamlitChla.py)
import streamlit as st
import sklearn
st.set_page_config(page_title="Plant Nutrient Prediction Website", page_icon="🧊", layout="wide")
#...........HEADER SECTION.............
with st.container():
    st.title("Predict Plant Nutrients")
    st.write("Hello! Thank you for using this web app. This web app is still a prototype under improvement. Kindly leave a comment based on your experience and the accuracy of the predictions.")
    
#........More Information about using the website..............
with st.container():
    st.write("---")
    st.header("Plant Chlorophyll prediction")
    st.write("Input the values of each of the **nutrients in percentage form** and the Chlorophyll concentration will be automatically computed and displayed below as 'Predicted Chlorophyll Content'.")
    st.write("**NOTE**: for 'Crops' field, the entries should be **0, 1 and 2 only**; for these crops **Corn = 0**; **Sorghum = 1**, and **Soybeans = 2**. So far, these are the only plants on which the model was trained.")

import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import joblib  # For loading the pre-trained model
import requests
import os

# Chlorophyll Prediction Section
with st.container():
    st.write("---")
    st.subheader("Plant Chlorophyll Prediction")
    # Load the pre-trained model
    loaded_model_chl = load_model('Random_Forest_Chl_model.pkl')

    # Get user input for nutrient content
    user_input_chl = get_user_input(['N', 'P', 'K', 'Ca', 'Mg', 'S', 'Crop'])

    # Submit button to trigger prediction
    if st.button('Submit Chlorophyll Prediction'):
        # Validate nutrient values to be percentages
        valid_inputs_chl = all(0.0 <= user_input_chl[nutrient] <= 100.0 for nutrient in nutrient_columns if nutrient != 'Crop')

        if not valid_inputs_chl:
            st.error("Please enter nutrient values in percentage form (0 to 100).")
        else:
            # Convert user input to DataFrame
            user_input_df_chl = pd.DataFrame([user_input_chl])

            # Make predictions
            prediction_chl = make_predictions(loaded_model_chl, user_input_df_chl)

            # Display the prediction
            st.write(f"**The predicted Chlorophyll content is:**", prediction_chl[0], "%")

# Nitrogen Prediction Section
with st.container():
    st.write("---")
    st.subheader("Plant Nitrogen Prediction")
    # Load the pre-trained model
    loaded_model_n = load_model('Random_Forest_N_model.pkl')

    # Get user input for nutrient content
    user_input_n = get_user_input(['P', 'K', 'Ca', 'Mg', 'S', 'Crop'])

    # Submit button to trigger prediction
    if st.button('Submit Nitrogen Prediction'):
        # Validate nutrient values to be percentages
        valid_inputs_n = all(0.0 <= user_input_n[nutrient] <= 100.0 for nutrient in nutrient_columns if nutrient != 'Crop')

        if not valid_inputs_n:
            st.error("Please enter nutrient values in percentage form (0 to 100).")
        else:
            # Convert user input to DataFrame
            user_input_df_n = pd.DataFrame([user_input_n])

            # Make predictions
            prediction_n = make_predictions(loaded_model_n, user_input_df_n)

            # Display the prediction
            st.write(f"**The predicted Nitrogen content is:**", prediction_n[0], "%")

# ... Repeat for other nutrients

# More Information Section
with st.container():
    st.write("---")
    st.subheader("Contact me")
    st.write("Email: ioyeg002@fiu.edu; Tel: (786) 710 0470")

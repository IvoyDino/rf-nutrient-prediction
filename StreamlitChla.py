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
    st.write("**NOTE**: fill the 'Crops' field, as follows: **Camelina = 0, Corn = 1, Sorghum = 2, Soy = 3, Strawberries = 4, Dragon fruit = 5, Tomatoes = 6, Sunn hemp = 7**.")

import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import joblib  # For loading the pre-trained model
import requests
import os

# Function to load a pre-trained model
def load_model(model_path):
    current_directory = os.getcwd()
    model_path = os.path.join(current_directory, model_path)
    return joblib.load(model_path)

# Function to get user input for nutrient content
def get_user_input(nutrient_columns):
    user_input = {}
    for nutrient in nutrient_columns:
        if nutrient == 'Crop':
            # Restrict input values for 'Crop' nutrient based on the model
            user_input[nutrient] = st.number_input(f'Enter {nutrient} value:', min_value=0, max_value=2, step=1, value=0, key=f'{nutrient}_input')
        else:
            user_input[nutrient] = st.number_input(f'Enter {nutrient} content (in percentage):', min_value=0.0, max_value=100.0, value=0.0, key=f'{nutrient}_input')
    return user_input

# Function to make predictions
def make_predictions(loaded_model, user_input_df):
    return loaded_model.predict(user_input_df)

# Streamlit app configuration
st.set_page_config(page_title="Plant Nutrient Prediction Website", page_icon="🧊", layout="wide")

# Header Section
with st.container():
    st.title("Predict Plant Nutrients")
    st.write("Hello! Thank you for using this web app. This web app is still a prototype under improvement. Kindly leave a comment based on your experience and the accuracy of the predictions.")

# Chlorophyll Prediction Section
with st.container():
    st.write("---")
    st.header("Plant Chlorophyll Prediction")
    # Load the pre-trained model
    loaded_model = load_model('Random_Forest_Chl_model.pkl')

    # Get user input for nutrient content
    user_input = get_user_input(['N', 'P', 'K', 'Ca', 'Mg', 'S', 'Crop'])

    # Submit button to trigger prediction
    if st.button('Submit Chlorophyll Prediction'):
        # Validate nutrient values to be percentages
        valid_inputs = all(0.0 <= user_input[nutrient] <= 100.0 for nutrient in nutrient_columns if nutrient != 'Crop')

        if not valid_inputs:
            st.error("Please enter nutrient values in percentage form (0 to 100).")
        else:
            # Convert user input to DataFrame
            user_input_df = pd.DataFrame([user_input])

            # Make predictions
            prediction = make_predictions(loaded_model, user_input_df)

            # Display the prediction
            st.write(f"**The predicted Chlorophyll content is:**", prediction[0], "%")

# Nutrient Prediction Sections
nutrient_columns = ['N', 'P', 'K', 'Ca', 'Mg', 'S', 'Crop']
nutrient_model_paths = ['Nitrogen_Random_Forest_model.pkl', 'Phosphorus_Random_Forest_model.pkl', 'Potassium_Random_Forest_model.pkl', 'Calcium_Random_Forest_model.pkl', 'Magnesium_Random_Forest_model.pkl', 'Sulphur_Random_Forest_model.pkl']

for nutrient, model_path in zip(nutrient_columns[:-1], nutrient_model_paths):
    with st.container():
        st.write("---")
        st.header(f"Plant {nutrient} Prediction")
        # Load the pre-trained model
        loaded_model = load_model(model_path)

        # Get user input for nutrient content
        user_input = get_user_input(nutrient_columns[:-1])

        # Submit button to trigger prediction
        if st.button(f'Submit {nutrient} Prediction'):
            # Validate nutrient values to be percentages
            valid_inputs = all(0.0 <= user_input[nutrient] <= 100.0 for nutrient in nutrient_columns if nutrient != 'Crop')

            if not valid_inputs:
                st.error(f"Please enter nutrient values in percentage form (0 to 100) for {nutrient}.")
            else:
                # Convert user input to DataFrame
                user_input_df = pd.DataFrame([user_input])

                # Make predictions
                prediction = make_predictions(loaded_model, user_input_df)

                # Display the prediction
                st.write(f"**The predicted {nutrient} content is:**", prediction[0], "%")

with st.container():
    st.write("---")
    st.subheader("Contact me")
    st.write("Email: ioyeg002@fiu.edu; Tel: (786) 710 0470")

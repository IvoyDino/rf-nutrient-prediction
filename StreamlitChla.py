# Streamlit app script (StreamlitChla.py)
import streamlit as st
import sklearn
st.set_page_config(page_title="Plant Nutrient Prediction Website", page_icon="🧊", layout="wide")
#...........HEADER SECTION.............
with st.container():
    st.title("Predict Plant Nutrients")
    st.write("Hello! Thank you for using this web app. This web app is still a prototype under improvement. Kindly leave a comment based on your experience and the accuracy of the predictions.")
    
#........More Information about using the website.............. 
import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import joblib  # For loading the pre-trained model
import os

def load_model(model_filename):
    model_path = os.path.join(os.getcwd(), model_filename)
    loaded_model = joblib.load(model_path)
    return loaded_model

def get_user_input(nutrient_columns, suffix=''):
    user_input = {}
    for nutrient in nutrient_columns:
        key = f'{nutrient}_{suffix}_{st._get_widget_id()}'
        if nutrient == 'Crop':
            user_input[nutrient] = st.number_input(f'Enter {nutrient} value:', min_value=0, max_value=2, step=1, value=0, key=key)
        else:
            user_input[nutrient] = st.number_input(f'Enter {nutrient} content (in percentage):', min_value=0.0, max_value=100.0, value=0.0, key=key)
    return user_input

def make_prediction(loaded_model, user_input_df):
    prediction = loaded_model.predict(user_input_df)
    return prediction

# Chlorophyll Prediction
with st.container():
    st.write("---")
    st.header("Plant Chlorophyll prediction")
    st.write("Input the values of each of the **nutrients in percentage form** and the Chlorophyll concentration will be automatically computed and displayed below as 'Predicted Chlorophyll Content'.")
    st.write("**NOTE**: for 'Crops' field, the entries should be **0, 1 and 2 only**; for these crops **Corn = 0**; **Sorghum = 1**, and **Soybeans = 2**. So far, these are the only plants on which the model was trained.")

# Load Chlorophyll Model
chlorophyll_model = load_model('Random_Forest_Chl_model.pkl')
nutrient_columns_chl = ['N', 'P', 'K', 'Ca', 'Mg', 'S', 'Crop']
user_input_chl = get_user_input(nutrient_columns_chl)

# Submit button for Chlorophyll Prediction
if st.button('Submit for Chlorophyll Prediction'):
    valid_inputs_chl = all(0.0 <= user_input_chl[nutrient] <= 100.0 for nutrient in nutrient_columns_chl if nutrient != 'Crop')
    if not valid_inputs_chl:
        st.error("Please enter nutrient values in percentage form (0 to 100).")
    else:
        user_input_df_chl = pd.DataFrame([user_input_chl])
        prediction_chl = make_prediction(chlorophyll_model, user_input_df_chl)
        st.write("**The predicted Chlorophyll content is:**", prediction_chl[0])

# Nitrogen Prediction
with st.container():
    st.write("---")
    st.header("Plant Nitrogen prediction")
    st.write("Input the values of each of the **nutrients in percentage form** and the Nitrogen concentration will be automatically computed and displayed below as 'Predicted Nitrogen Content'.")
    st.write("**NOTE**: for 'Crops' field, the entries should be **0, 1 and 2 only**; for these crops **Corn = 0**; **Sorghum = 1**, and **Soybeans = 2**. So far, these are the only plants on which the model was trained.")

# Load Nitrogen Model
nitrogen_model = load_model('Nitrogen_Random_Forest_model.pkl')
nutrient_columns_nitrogen = ['P', 'K', 'Ca', 'Mg', 'S', 'Crop']
user_input_nitrogen = get_user_input(nutrient_columns_nitrogen)

# Submit button for Nitrogen Prediction
if st.button('Submit Nitrogen Prediction'):
    valid_inputs_nitrogen = all(0.0 <= user_input_nitrogen[nutrient] <= 100.0 for nutrient in nutrient_columns_nitrogen if nutrient != 'Crop')
    if not valid_inputs_nitrogen:
        st.error("Please enter nutrient values in percentage form (0 to 100).")
    else:
        user_input_df_nitrogen = pd.DataFrame([user_input_nitrogen])
        prediction_nitrogen = make_prediction(nitrogen_model, user_input_df_nitrogen)
        st.write("**The predicted Nitrogen content is:**", prediction_nitrogen[0], "%")

# Contact Section
with st.container():
    st.write("---")
    st.subheader("Contact me")
    st.write("Email: ioyeg002@fiu.edu; Tel: (786) 710 0470")

# Streamlit app script (StreamlitChla.py)
import streamlit as st
import sklearn
st.set_page_config(page_title="Chlorophyll Prediction Website", page_icon="🧊", layout="wide")

#...........HEADER SECTION.............
with st.container():
    st.subheader("Prediction of Chlorophyll content in plants")
    st.title("Machine Learning approach using Random Forest Model")
    st.write("The study was conducted by **Ivan Oyege** from Florida International Univeristy, and the data used in the predicition was from Dr. Yufeng Ge, from University of Nebraska-Lincoln and the link to the paper in which the data was first used is given in the link below")
    st.write("[Learn more in this paper>](https://academic.oup.com/jxb/article/74/14/4050/7109174)")

#........More Information about using the website..............
with st.container():
    st.write("---")
    st.header("How to input your nutrient data")
    st.write("Input the values of each of the **nutrients in percentage form** and the Chlorophyll concentration will be automatically computed and displayed below under 'Predicted Chlorophyll Content'.")
    st.write("**NOTE**: for 'Crops' field, the entries should be **whole numbers; 0, 1 and 2 only** as follows: **Corn = 0**; **Sorghum = 1**, and **Soybeans = 2**. So far these are the only plants on which the model was trained.")


import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import joblib  # For loading the pre-trained model
import requests
import os


# In[3]:


# Load the pre-trained Random Forest model
model_path = 'Random_Forest_Chl_model.pkl'
# Get the current working directory
current_directory = os.getcwd()

# Specify the relative path to the model file
model_path = os.path.join(current_directory, 'Random_Forest_Chl_model.pkl')

# Load the pre-trained Random Forest model
loaded_model = joblib.load(model_path)

# Example input fields (replace with actual nutrient names)
nutrient_columns = ['N', 'P', 'K', 'Ca', 'Mg', 'S', 'Crop']

# Get user input for nutrient content
user_input = {}
for nutrient in nutrient_columns:
    if nutrient == 'Crop':
        # Restrict input values for 'Crop' nutrient to whole numbers between 0 and 2
        user_input[nutrient] = st.number_input(f'Enter {nutrient} content:', min_value=0, max_value=2, step=1, value=0)
    else:
        user_input[nutrient] = st.number_input(f'Enter {nutrient} content (in percentage):', min_value=0.0, max_value=100.0, value=0.0)

# Submit button to trigger prediction
if st.button('Submit'):
    # Validate nutrient values to be percentages
    valid_inputs = all(0.0 <= user_input[nutrient] <= 100.0 for nutrient in nutrient_columns if nutrient != 'Crop')

    if not valid_inputs:
        st.error("Please enter nutrient values in percentage form (0 to 100).")
    else:
        # Convert user input to DataFrame
        user_input_df = pd.DataFrame([user_input])

        # Make predictions
        prediction = loaded_model.predict(user_input_df)

        # Display the prediction
        st.write("**The predicted Chlorophyll content is:**", prediction[0])

               
with st.container():
    st.write("---")
    st.subheader("Contact me")
    st.write("Email: ioyeg002@fiu.edu; Tel: (786) 710 0470")

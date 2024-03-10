# Streamlit app script (StreamlitChla.py)
import streamlit as st
import sklearn
st.set_page_config(page_title="Plant Nutrient Prediction Website", page_icon="🧊", layout="wide")
#website tracking
# Google Analytics Measurement ID
measurement_id = "G-7N6H5T3X3L"  # Replace with your actual Measurement ID

# Google Analytics tracking code
ga_code = f"""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={measurement_id}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{measurement_id}');
</script>
"""

# Create an empty container and add the tracking code without rendering it visibly
container = st.empty()
container.markdown(ga_code, unsafe_allow_html=True)

#...........HEADER SECTION.............
with st.container():
    st.title("Predict Plant Nutrients")
    st.write("Hello! Thank you for using this web app developed by Ivan Oyege. This app is under testing and the predictions may not be 100% accurate. However, your feedback will help in improving it. Kindly leave a comment in the 'Contact Me' section at the bottom of the page, based on your experience and the accuracy of the predictions. You can use the app to predict **Chlorophyll, Nitrogen, Phosphorus, Potassium, Calcium, Magnesium, and Sulfur** content in plants.")
    
#........More Information about using the website.............. 
import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import joblib  # For loading the pre-trained model
import os

# Use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

def load_model(model_filename):
    model_path = os.path.join(os.getcwd(), model_filename)
    loaded_model = joblib.load(model_path)
    return loaded_model

def get_user_input(nutrient_columns, suffix=''):
    user_input = {}
    widget_counter = 0  # Counter variable to ensure unique keys
    for nutrient in nutrient_columns:
        key = f'{nutrient}_{suffix}_{widget_counter}'
        widget_counter += 1
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

def load_chlorophyll_model():
    return load_model('Random_Forest_Chl_model.pkl')

# Load Chlorophyll Model
left_column, right_column = st.columns(2)
with left_column:
    chlorophyll_model = load_chlorophyll_model()
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

with right_column:
    st.empty()

    
# Nitrogen Prediction
with st.container():
    st.write("---")
    st.header("Plant Nitrogen prediction")
    st.write("Input the values of each of the **nutrients in percentage form** and the Nitrogen concentration will be automatically computed and displayed below as 'Predicted Nitrogen Content'.")
    st.write("**NOTE**: for 'Crops' field, the entries should be **0, 1 and 2 only**; for these crops **Corn = 0**; **Sorghum = 1**, and **Soybeans = 2**. So far, these are the only plants on which the model was trained.")

# Load Nitrogen Model
left_column, right_column = st.columns(2)
with left_column:
    nitrogen_model = load_model('Nitrogen_Random_Forest_model.pkl')
    nutrient_columns_nitrogen = ['P', 'K', 'Ca', 'Mg', 'S', 'Crop']
    user_input_nitrogen = get_user_input(nutrient_columns_nitrogen)
    
# Submit button for Nitrogen Prediction
if st.button('Submit for Nitrogen Prediction'):
    valid_inputs_nitrogen = all(0.0 <= user_input_nitrogen[nutrient] <= 100.0 for nutrient in nutrient_columns_nitrogen if nutrient != 'Crop')
    if not valid_inputs_nitrogen:
        st.error("Please enter nutrient values in percentage form (0 to 100).")
    else:
        user_input_df_nitrogen = pd.DataFrame([user_input_nitrogen])
        prediction_nitrogen = make_prediction(nitrogen_model, user_input_df_nitrogen)
        st.write("**The predicted Nitrogen content is:**", prediction_nitrogen[0], "%")
with right_column:
    st.empty()

# Phosphorus Prediction
with st.container():
    st.write("---")
    st.header("Plant Phosphorus prediction")
    st.write("Input the values of each of the **nutrients in percentage form** and the Phosphorus concentration will be automatically computed and displayed below as 'Predicted Phosphorus Content'.")
    st.write("**NOTE**: for 'Crops' field, the entries should be **0, 1 and 2 only**; for these crops **Corn = 0**; **Sorghum = 1**, and **Soybeans = 2**. So far, these are the only plants on which the model was trained.")

# Load Phosphorus Model
left_column, right_column = st.columns(2)
with left_column:
    phosphorus_model = load_model('Phosphorus_Random_Forest_model.pkl')
    nutrient_columns_phosphorus = ['N', 'K', 'Ca', 'Mg', 'S', 'Crop']
    user_input_phosphorus = get_user_input(nutrient_columns_phosphorus, suffix='phosphorus')

# Submit button for Phosphorus Prediction
if st.button('Submit for Phosphorus Prediction'):
    valid_inputs_phosphorus = all(0.0 <= user_input_phosphorus[nutrient] <= 100.0 for nutrient in nutrient_columns_phosphorus if nutrient != 'Crop')
    if not valid_inputs_phosphorus:
        st.error("Please enter nutrient values in percentage form (0 to 100).")
    else:
        user_input_df_phosphorus = pd.DataFrame([user_input_phosphorus])
        prediction_phosphorus = make_prediction(phosphorus_model, user_input_df_phosphorus)
        st.write("**The predicted Phosphorus content is:**", prediction_phosphorus[0], "%")
with right_column:
    st.empty()

# Potassium Prediction
with st.container():
    st.write("---")
    st.header("Plant Potassium prediction")
    st.write("Input the values of each of the **nutrients in percentage form** and the Potassium concentration will be automatically computed and displayed below as 'Predicted Potassium Content'.")
    st.write("**NOTE**: for 'Crops' field, the entries should be **0, 1 and 2 only**; for these crops **Corn = 0**; **Sorghum = 1**, and **Soybeans = 2**. So far, these are the only plants on which the model was trained.")

# Load Potassium Model
left_column, right_column = st.columns(2)
with left_column:
    potassium_model = load_model('Potassium_Random_Forest_model.pkl')
    nutrient_columns_potassium = ['N', 'P', 'Ca', 'Mg', 'S', 'Crop']
    user_input_potassium = get_user_input(nutrient_columns_potassium, suffix='potassium')

# Submit button for Potassium Prediction
if st.button('Submit for Potassium Prediction'):
    valid_inputs_potassium = all(0.0 <= user_input_potassium[nutrient] <= 100.0 for nutrient in nutrient_columns_potassium if nutrient != 'Crop')
    if not valid_inputs_potassium:
        st.error("Please enter nutrient values in percentage form (0 to 100).")
    else:
        user_input_df_potassium = pd.DataFrame([user_input_potassium])
        prediction_potassium = make_prediction(potassium_model, user_input_df_potassium)
        st.write("**The predicted Potassium content is:**", prediction_potassium[0], "%")

with right_column:
    st.empty()

# Sulfur Prediction
with st.container():
    st.write("---")
    st.header("Plant Sulfur prediction")
    st.write("Input the values of each of the **nutrients in percentage form** and the Sulfurs concentration will be automatically computed and displayed below as 'Predicted Sulfur Content'.")
    st.write("**NOTE**: for 'Crops' field, the entries should be **0, 1 and 2 only**; for these crops **Corn = 0**; **Sorghum = 1**, and **Soybeans = 2**. So far, these are the only plants on which the model was trained.")

# Load Sulfur Model
left_column, right_column = st.columns(2)
with left_column:
    sulfur_model = load_model('Sulphur_Random_Forest_model.pkl')
    nutrient_columns_sulfur = ['N', 'P', 'K', 'Ca', 'Mg', 'Crop']
    user_input_sulfur = get_user_input(nutrient_columns_sulfur, suffix='sulfur')

# Submit button for Sulfur Prediction
if st.button('Submit for Sulfur Prediction'):
    valid_inputs_sulfur = all(0.0 <= user_input_sulfur[nutrient] <= 100.0 for nutrient in nutrient_columns_sulfur if nutrient != 'Crop')
    if not valid_inputs_sulfur:
        st.error("Please enter nutrient values in percentage form (0 to 100).")
    else:
        user_input_df_sulfur = pd.DataFrame([user_input_sulfur])
        prediction_sulfur = make_prediction(sulfur_model, user_input_df_sulfur)
        st.write("**The predicted Sulfur content is:**", prediction_sulfur[0], "%")

with right_column:
    st.empty()

# Calcium Prediction
with st.container():
    st.write("---")
    st.header("Plant Calcium prediction")
    st.write("Input the values of each of the **nutrients in percentage form** and the Calcium concentration will be automatically computed and displayed below as 'Predicted Calcium Content'.")
    st.write("**NOTE**: for 'Crops' field, the entries should be **0, 1 and 2 only**; for these crops **Corn = 0**; **Sorghum = 1**, and **Soybeans = 2**. So far, these are the only plants on which the model was trained.")

# Load Calcium Model
left_column, right_column = st.columns(2)
with left_column:
    calcium_model = load_model('Calcium_Random_Forest_model.pkl')
    nutrient_columns_calcium = ['N', 'P', 'K', 'Mg', 'S', 'Crop']
    user_input_calcium = get_user_input(nutrient_columns_calcium, suffix='calcium')

# Submit button for Calcium Prediction
if st.button('Submit for Calcium Prediction'):
    valid_inputs_calcium = all(0.0 <= user_input_calcium[nutrient] <= 100.0 for nutrient in nutrient_columns_calcium if nutrient != 'Crop')
    if not valid_inputs_calcium:
        st.error("Please enter nutrient values in percentage form (0 to 100).")
    else:
        user_input_df_calcium = pd.DataFrame([user_input_calcium])
        prediction_calcium = make_prediction(calcium_model, user_input_df_calcium)
        st.write("**The predicted Calcium content is:**", prediction_calcium[0], "%")

with right_column:
    st.empty()

# Magnesium Prediction
with st.container():
    st.write("---")
    st.header("Plant Magnesium prediction")
    st.write("Input the values of each of the **nutrients in percentage form** and the Magnesium concentration will be automatically computed and displayed below as 'Predicted Magnesium Content'.")
    st.write("**NOTE**: for 'Crops' field, the entries should be **0, 1 and 2 only**; for these crops **Corn = 0**; **Sorghum = 1**, and **Soybeans = 2**. So far, these are the only plants on which the model was trained.")

# Load Magnesium Model
left_column, right_column = st.columns(2)
with left_column:
    magnesium_model = load_model('Magnesium_Random_Forest_model.pkl')
    nutrient_columns_magnesium = ['N', 'P', 'K', 'Ca', 'S', 'Crop']
    user_input_magnesium = get_user_input(nutrient_columns_magnesium, suffix='magnesium')

# Submit button for Magnesium Prediction
if st.button('Submit for Magnesium Prediction'):
    valid_inputs_magnesium = all(0.0 <= user_input_magnesium[nutrient] <= 100.0 for nutrient in nutrient_columns_magnesium if nutrient != 'Crop')
    if not valid_inputs_magnesium:
        st.error("Please enter nutrient values in percentage form (0 to 100).")
    else:
        user_input_df_magnesium = pd.DataFrame([user_input_magnesium])
        prediction_magnesium = make_prediction(magnesium_model, user_input_df_magnesium)
        st.write("**The predicted Magnesium content is:**", prediction_magnesium[0], "%")

with right_column:
    st.empty()

# Contact Section
with st.container():
    st.write("---")
    st.subheader("Contact me")
    st.write("Please give me some feedback based on your experience with the web app and any suggestions are welcome.")
    
#contact form
contact_form = """
<form action="https://formsubmit.co/oyege92@gmail.com" method="POST">
    <input type ="hidden" name="_captcha" value="false">
     <input type="text" name="Name" placeholder = "Your name" required>
     <input type="email" name="Email" placeholder = "Your email" required>
     <textarea name ="Message" placeholder = "Your message here" required></textarea>
     <button type="submit">Send</button>
</form> 
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()

import streamlit as st
import pandas as pd
import pickle

st.write("# Advertising Sales Predictor App")
st.write("This app predicts the **Sales** of Different Media!")

st.sidebar.header('User Input Parameters')

def user_input_features():
    TV = st.sidebar.slider('TV', 0.7, 296.4, 100.0)
    Radio = st.sidebar.slider('Radio', 0.0, 49.6, 25.0)
    Newspaper = st.sidebar.slider('Newspaper', 0.3, 114.0, 60.0)
    data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper,}
    return data

df = user_input_features()

st.subheader('User Input Parameter')
st.write(df)


file_path = "Sales-Model-ARNN-Project-V3.h5"

try:
    with open(file_path, "rb") as file:
        loaded_model = pickle.load(file)

  
    input_data = pd.DataFrame(df, index=[0])
    
    input_data['MissingFeature'] = 0 
    
    prediction = loaded_model.predict(input_data.values)

st.subheader('Prediction')
st.write(prediction)

except FileNotFoundError:
    st.error("Model file "Sales-Model-ARNN-Project-V3.h5" not found. Please make sure the file exists.")
except Exception as e:
    st.error(f"An error occurred: {e}")

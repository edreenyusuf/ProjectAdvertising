import streamlit as st
import pandas as pd
import seaborn as sns
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
            'Newspaper': Newspaper}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input Parameter')
st.write(df)

#prediction = pickle.load(open("Sales-Model-ARNN-Project-V3.h5", "rb")
                         


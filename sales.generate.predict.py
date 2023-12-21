import streamlit as st
import pandas as pd
import seaborn as sns

st.write("# Advertising Sales Predictor App")
st.write("This app predicts the **Sales** of Media Type!")

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Tv', 0.7, 296.4, 100.0)
    sepal_width = st.sidebar.slider('Radio', 0.0, 49.6, 25.0)
    petal_length = st.sidebar.slider('Newspaper', 0.3, 114.0, 60.0)
    data = {'Tv': Tv,
            'Radio': Radio,
            'Newspaper': Newspaper}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()


st.subheader('Class labels and their corresponding index number')
st.write(Y.unique())

st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)

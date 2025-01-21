import streamlit as st
import pandas as pd
import joblib as jl

model = jl.load('house_price_prediction_model.pkl')

st.title('House Price Predictor Model')

area = st.number_input('Area Required in Square Feet')
bedrooms = st.number_input('Number of Bedrooms')
bathrooms = st.number_input('Number of Bathrooms')
input_data = pd.DataFrame({
    'area': [area],
    'bedrooms': [bedrooms],
    'bathrooms': [bathrooms],
})

if st.button('Predict'):
    price_prediction = model.predict(input_data)
    st.write(f'Estimated House Price: {price_prediction[0]:.2f}')

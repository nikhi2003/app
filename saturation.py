import streamlit as st
import pickle
spo2=pickle.load(open('sat.pkl', 'rb'))

st.write('Enter the following features for the prediction:')

age = st.sidebar.number_input('Enter your age: ')
BMI=st.sidebar.number_input('Enter your BMI: ')
diabetes=st.sidebar.number_input('Enter 1 if you have diabetes and 0 if not')
s_bp=st.sidebar.number_input('Enter your Systolic BP: ')
d_bp=st.sidebar.number_input('Enter your Diastolic BP: ')
resp=st.sidebar.number_input('Enter your Respiratory rate: ')
hrate=st.sidebar.number_input('Enter your heart rate : ')

if st.button('Make Prediction'):
    # we are taking inputs here and use it for the prediction of spo2
    features = [[age,BMI,diabetes,s_bp,d_bp,resp, hrate]]

    result = spo2.predict(features)[0]
    st.write('Predicted SPO2:', result)

# Project 8: Create a Python Streamlit BMI Calculator Web App in Just 6 Minutes

import streamlit as st

st.title("BMI Calculator")

height = st.slider("Enter your Height (in cm):", 100 , 250, 175) 
weight = st.slider("Enter your Height (in kg):", 40, 200, 70)

bmi = weight / ((height/200) ** 2)

st.write(f"Your BMI is {bmi:.2f}")

st.write("### BMI Categories ###")
st.write("- Underweight: BMI less than 18.5")
st.write("- Normal weight: BMI between 18.5 and 24.9")
st.write("- Overweight: BMI between 25 and 29.9")
st.write("- Obesity: BMI 30 or greater")
import streamlit as st
import pandas as pd
st.title("Welcome")
st.write("This is my first streamlit application")
data = pd.read_csv(r"C:\Users\niraj\OneDrive\Desktop\solar_power_predictino\solar_power_output.csv")
st.write(data)
st.line_chart(data)

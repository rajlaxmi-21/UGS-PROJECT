import streamlit as st
import requests

st.title("🌳 Deforestation Monitoring System")

st.write("Public Dashboard")

location = st.text_input("Enter Location")

# if st.button("Analyze"):
#     st.write(f"Analyzing {location}...")


if st.button("Analyze"):
    response = requests.post("http://127.0.0.1:8000/analyze-location")
    st.json(response.json())
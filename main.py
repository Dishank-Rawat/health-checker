import streamlit as st

st.header("Welcome to this daily health checker app")
st.write("Made by Dishank Rawat")

st.text_input("Please enter your name")
st.number_input("Please enter your age", 0, 100)

st.number_input("Please enter how many hours of sleep do you get", 0, 24)

st.number_input("Please enter how many glasses of water you consume", 0, 50)

st.number_input("Please enter your daily exercise duration (in hours)", 0, 8)

st.number_input("Please enter your daily screen time (in hours)", 0, 24)

st.selectbox("Please select your current mood", ["Happy", "Sad", "Stressed", "Energetic"])

import streamlit as st

st.header("Welcome to this daily health checker app")
st.write("Made by Dishank Rawat")

name = st.text_input("Please enter your name")
age = st.number_input("Please enter your age", 0, 100)

sleep = st.number_input("Please enter how many hours of sleep do you get", 0, 24)

water = st.number_input("Please enter how many glasses of water you consume", 0, 50)

exercise = st.number_input("Please enter your daily exercise duration (in hours)", 0, 8)

screentime = st.number_input("Please enter your daily screen time (in hours)", 0, 24)

mood = st.selectbox("Please select your current mood", ["Happy", "Sad", "Stressed", "Energetic"])

wellness = 100
if age >= 80:
  wellness -= 5

if sleep <= 8 or sleep >= 12:
  wellness -= 5

if water <= 7 or water >= 16:
  wellness -= 10

if exercise <= 0.5:
  wellness -= 10

if screentime > 2:
  wellness -= screentime * 5

if mood == "Happy":
  wellness += 10
elif mood == "Sad":
  wellness -= 5
elif mood == "Stressed":
  wellness -= 10
else:
  wellness += 5

st.write(f"{name}: Wellness score for today is: {wellness}")
st.progress(wellness)


import streamlit as st

st.header("Welcome to this daily health checker app")
st.write("Made by Dishank Rawat")

with st.form("health_form"):

    name = st.text_input("Please enter your name", key="name")
    age = st.number_input("Please enter your age", 0, 100, key="age")

    sleep = st.number_input("Please enter how many hours of sleep do you get", 0, 24, key="sleep")

    water = st.number_input("Please enter how many glasses of water you consume", 0, 50, key="water")

    exercise = st.number_input("Please enter your daily exercise duration (in hours)", 0.0, 8.0, key="exercise")

    screentime = st.number_input("Please enter your daily screen time (in hours)", 0, 24, key="screentime")

    mood = st.selectbox("Please select your current mood", ["Happy", "Sad", "Stressed", "Energetic"], key="mood")

    submit = st.form_submit_button("Check Wellness")

if submit:

    wellness = 100

    if age >= 80:
        wellness -= 5

    if sleep < 8 or sleep > 12:
        wellness -= 5

    if water < 7 or water > 16:
        wellness -= 10

    if exercise <= 0.5:
        wellness -= 10
    else:
        wellness += 3 * exercise

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

    wellness = max(0, min(100, int(wellness)))

    st.write(f"{name}, your wellness score for today is: {wellness}")

    st.progress(wellness)

    if wellness >= 80:
        st.success("Excellent, keep maintaining your healthy habits.")
    elif wellness >= 50:
        st.warning("Good effort. There is room for improvement.")
    else:
        st.error("Try to improve your daily health habits.")

if st.button("Clear Form"):

    if "name" in st.session_state:
        del st.session_state.name

    if "age" in st.session_state:
        del st.session_state.age

    if "sleep" in st.session_state:
        del st.session_state.sleep

    if "water" in st.session_state:
        del st.session_state.water

    if "exercise" in st.session_state:
        del st.session_state.exercise

    if "screentime" in st.session_state:
        del st.session_state.screentime

    if "mood" in st.session_state:
        del st.session_state.mood

    st.rerun()

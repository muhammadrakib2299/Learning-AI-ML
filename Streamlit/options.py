import streamlit as st

st.header("Options Selections")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0, max_value=120, step=1)
gender = st.selectbox("Select your gender", ["Male", "Female", "Other"])    
hobbies = st.multiselect("Select your hobbies", ["Reading", "Traveling", "Cooking", "Sports", "Music"])
if st.button("Submit"):
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"Gender: {gender}")
    st.write(f"Hobbies: {', '.join(hobbies)}")    
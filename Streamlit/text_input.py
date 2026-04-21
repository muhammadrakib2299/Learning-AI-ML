import streamlit as st

st.title("My first Streamlit app", anchor=False)
st.header("This is a header", divider=True)

st.subheader("This is a subheader")
st.text("This is some text")
st.markdown("This is some markdown text")
st.markdown("This is some :orange[**bold**] text")

st.divider()


name = st.text_input("Enter your name", placeholder="Type your name here")

st.write(f"Hello, Your name is {name}!")

st.divider()

age = st.number_input("Enter your age",  min_value=0, max_value=120, step=1)
st.write(f"Your age is {age} years old.")

st.divider()

password = st.text_input("Enter your password", type="password")
st.write(f"Your password is {password}")    
import streamlit as st

st.title("Media Element")

st.divider()

img = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if img is not None:
    st.image(img)       
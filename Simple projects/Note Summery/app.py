import streamlit as st

st.title("Note Summarizer and Quiz Generator App")
st.markdown('Upload upto 3 images to generate Note Summaries and Quizzes.')
st.divider()


with st.sidebar:
    images =  st.file_uploader(
        'Uplaod your images here (max 3)',
        type=['jpg', 'jpeg', 'png'],
        accept_multiple_files=True
    )

    if images:
        st.subheader('Uploaded Images')
        if len(images) > 3:
            st.warning('Please upload a maximum of 3 images.')
        else:
            col = st.columns(len(images))
            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)

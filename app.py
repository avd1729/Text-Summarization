import streamlit as st
import joblib

model = joblib.load('model.pkl')
st.title('Text-Summarizer ⚡')

text = st.text_input('Text to be summarized')


def predict():
    predition = model(text, max_length=130, min_length=30, do_sample=False)
    st.success(predition)


trigger = st.button('Summarize', on_click=predict)

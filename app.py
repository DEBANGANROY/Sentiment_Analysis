import streamlit as st
import joblib
model = joblib.load('/content/drive/MyDrive/ml samrtknower/major project/Sentiment Analysis')
st.title('Sentiment Analyzer')
ip = st.text_input("Enter message")
op = model.predict([ip])
if st.button('Analyze'):
  st.title(op[0])

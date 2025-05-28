import streamlit as st
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model

Word_Index = imdb.get_word_index()
Reversed_Words_Index = {value:key for key,value in Word_Index.items()}

Model = load_model("IMDB.h5")

def decode_review(encoded_review):
    return " ".join([Reversed_Words_Index.get(1 - 3, "?") for i in encoded_review])

def process_text(text):
    Words = text.lower().split()
    encoded_review = ([Word_Index.get(word, 2) + 3 for word in Words])
    padded_review = sequence.pad_sequences([encoded_review] , maxlen=500)
    return padded_review

    
    return sentiment, prediction[0][0]

st.title("Movie Review Analysis")
st.write("Write review to be categorized as Positve or Negative")

User_input = st.text_area("Movie Review")

if st.button("Classify"):
    preprocessed = process_text(User_input)
    Prediction = Model.predict(preprocessed)
    sentiment = "Positive" if Prediction[0][0] > 0.8 else "Negative"
    
    st.write(f"Review is : {sentiment}")
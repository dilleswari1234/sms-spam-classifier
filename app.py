import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load your trained model and feature extraction
with open('your_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('your_vectorizer.pkl', 'rb') as vectorizer_file:
    feature_extraction = pickle.load(vectorizer_file)

# Streamlit app
st.title("Sms Spam Detection")

# Input email from the user
input_mail = st.text_area("Enter the sms text:", "")

if st.button("Predict"):
    if input_mail.strip() == "":
        st.write("Please enter some text to predict.")
    else:
        # Convert text to feature vectors
        input_data_features = feature_extraction.transform([input_mail])

        # Make prediction
        prediction = model.predict(input_data_features)

        if prediction[0] == 1:
            st.success("Not a Spam")
        else:
            st.error("Spam")

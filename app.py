import streamlit as st
import nltk
import torch
from transformers import pipeline

# Initialize the chatbot pipeline
chatbot = pipeline("text-generation", model="distilgpt2")

# Function to handle user input and provide responses
def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "Please Contact Doctor for accurate advice"
    elif "appointment" in user_input:
        return "Would you like to schedule an appointment with the doctor?"
    elif "medication" in user_input:
        return "It's important to take prescribed medicines regularly.If you have concerns, consult your doctor."
    else:
        # Corrected argument names and removed unnecessary argument
        response = chatbot(user_input, max_length=500)
    
        return response[0]['generated_text']

# Main function to run the Streamlit app
def main():
    st.title("Healthcare Assistance Chatbot")
    user_input = st.text_input("How can I assist you today?")
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            with st.spinner("Processing your query, Please wait..."):
                response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant: ", response)
            print(response)
        else:
            st.write("Please enter a message to get a response.")

# Run the main function
if __name__ == "__main__":
    main()
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the Gemini model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

# Function to load Gemini Pro model and get responses
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")

# Initialize session state for input
if 'input' not in st.session_state:
    st.session_state.input = ''

# If the clear button is pressed, clear the input before the widget is created
if st.button("Clear"):
    st.session_state.input = ''

st.header("Gemini LLM Application")

# Text input field, bound to the session state
input = st.text_input("Input:", value=st.session_state.input, key="input")

# Submit button
submit = st.button("Ask the Question")

# If the submit button is pressed
if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)

from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#funtion to load gemimi pro model and get response
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemimi_response(question):
    response = chat.send_message(question, stream=True) #stream=True for chat history
    return response

# initialize streamlit app
st.set_page_config(page_title="QnA chat")
st.header("Gemini LLM application version")

# initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
    
input = st.text_input("Input: ", key='input')
submit = st.button('Ask Question')

if input and submit:
    response = get_gemimi_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(('Bot',chunk.text))

st.subheader("The Chat History is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
        
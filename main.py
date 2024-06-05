from streamlit_mic_recorder import mic_recorder,speech_to_text
import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

open_api_key = os.getenv('OPENAI_API_KEY')


st.title("My AI Voice Assistent")
st.write("AI Voice Assistent using Langchain and Streamlit.")

llm = ChatOpenAI(temperature=0.7, model = 'gpt-4o', max_tokens=1000, openai_api_key=open_api_key)
# audio = mic_recorder(start_prompt="Start Recording")
#
# if audio:
#     st.audio(audio["bytes"])


text = speech_to_text(language="en", use_container_width=True, just_once=True, key="STT")
st.write(f"SALMAN:{text}")
if text:
    response = llm.invoke(text)
    st.write(f"GPT:{response.content}")
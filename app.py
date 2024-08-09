import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from src.helper import get_text, get_video_id
from src import *

load_dotenv()

# Initialize the Google Generative AI model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# Define the notes generation prompt template
notes_template = PromptTemplate(
    input_variables=["Text"],  
    template=summarizer  # Assuming 'summarizer' is defined elsewhere
)

# Create the LLMChain with the prompt and model
notes_chain = LLMChain(llm=llm, prompt=notes_template, verbose=True)

# Streamlit page configuration
st.set_page_config(page_title="Youtube Notes", page_icon="", layout="centered")

st.title("YouTube Detailed Notes")

# Sidebar for input
with st.sidebar:
    st.header("Upload a link")
    url = st.text_input("Link", max_chars=100, placeholder="e.g. https://www.youtube.com/watch?v=8fX3rOjTloc")
    generate_button = st.button("Create Notes")

if generate_button:
    if url:
        with st.spinner("Generating Notes..."):
            try:
                # Extract video ID and text from the YouTube link
                video_id = get_video_id(url)
                text = get_text(video_id)

                # Generate notes using the LLMChain
                response = notes_chain({"Text": text})

                # Display the generated notes
                st.markdown(response['text'])
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
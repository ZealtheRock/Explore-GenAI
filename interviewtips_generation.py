from gc import set_debug

from langchain_community.chat_models import ChatOllama
import streamlit as st
from langchain_core.prompts import PromptTemplate

#from openai_demo import response

# OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")
# Make sure the LLM is running locally with the command: ollama serve, 'ollama pull gemma:2b'
llm = ChatOllama(model="mistral")
# For open source LLM model you need not pass the API_KEY, but for the OpenAI model you need to pass the API_KEY.
prompt = PromptTemplate(
    input_variables=["Company_Name","Position_Title","Your_Strength","Your_Weakness"],
    template=""" You are a career coach.Provide tailored interview tips for Position Title: {Position_Title} at {Company_Name}.
    Highlight you strength in {Your_Strength} and prepare for question about your weakness in {Your_Weakness}.
      """,
)
# Setting debug mode to True to see detailed logs and debug information

st.title("Interview Tips Generator with Mistral LLM...")
Company = st.text_input("Enter the Company Name to explore its interview tips:")
position = st.number_input("Enter the position")
Strength = st.text_area("Enter your strength", height=100)
Weakness = st.text_area("Enter your weakness", height=100)
if Company and position and Strength and Weakness:
    response = llm.invoke(prompt.format(Company=Company, position=position, Strength=Strength, Weakness=Weakness))
    st.write(response.content) # to get the response only not the metadata

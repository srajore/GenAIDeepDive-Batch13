from langchain_ollama import ChatOllama
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
from dotenv import load_dotenv

load_dotenv(override=True)

#-------------------------------------------------------------
# Streamlit page setup

st.set_page_config(page_title="Achievements Finder", page_icon="🎯")

st.title(" Find Key Achievements using langchain + ollama")

st.write(" Enter person name and category (e.g., politics, science, sports) to get key achievements in bulleted points. ")

#--------------User Input Section--------------------------------

person = st.text_input(" Enter the name of the person: ")

category = st.text_input(" Enter the category (e.g., politics, science, sports): ")

#----------------- Button to trigger the LLM call ----------------------

if st.button(" Get Achievements "):
    if not person or not category:
        st.warning(" Please enter both person name and category.")
    else:
        with st.spinner(" Fetching achievements... "):
            try:
                prompt = ChatPromptTemplate.from_messages([
                ("system", "you are a helpful assistant."),
                ("user", "Tell me a key achivements of {person} in 4 bulleted points in {category} and If you don't know the answer please Say I don't have any information about person/category")
                ])

                #llm = ChatOllama(model="llama3.2:latest")
                llm = GoogleGenerativeAI(model="gemini-2.5-pro")

                chain = prompt | llm

                response = chain.invoke({"person": person, "category": category})

                # Display the response
                st.write(response)

            except Exception as e:
                st.error(f"An error occurred: {e}")


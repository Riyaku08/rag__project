import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, OpenAI

# Title
st.title(" RAG Chatbot")

# API key
api_key = "your api key"

# Load PDF
loader = PyPDFLoader("data.pdf")
documents = loader.load()

# Embeddings
embeddings = OpenAIEmbeddings(api_key=api_key)

# Vector DB
db = FAISS.from_documents(documents, embeddings)

# LLM
llm = OpenAI(api_key=api_key)

# User input
query = st.text_input("Ask something about the document:")

# Button
if st.button("Get Answer"):
    if query:
        docs = db.similarity_search(query)

        response = llm.invoke(
            f"Answer this based on context: {docs[0].page_content} \n Question: {query}"
        )

        st.write("### Answer:")
        st.write(response)

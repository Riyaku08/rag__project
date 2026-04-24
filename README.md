# 📄 RAG Chatbot (AI Project)

This project is a Retrieval-Augmented Generation (RAG) chatbot built using LangChain and OpenAI.

##  Features
- Chat with PDF documents
- Semantic search using FAISS
- Interactive UI using Streamlit
- Fast response with caching

## Tech Stack
- Python
- LangChain
- OpenAI API
- FAISS
- Streamlit

## How to Run

1. Install dependencies:
pip install langchain openai faiss-cpu streamlit

2. Set API key:
setx OPENAI_API_KEY "your-api-key"

3. Run CLI:
python main.py

4. Run UI:
streamlit run app.py

##  Use Case
You can upload any PDF (like resume, notes) and ask questions from it.

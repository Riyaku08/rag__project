from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, OpenAI

# API key 
api_key = "your api key"

# Load PDF
loader = PyPDFLoader("data.pdf")
documents = loader.load()

# Create embeddings
embeddings = OpenAIEmbeddings(api_key=api_key)

# Store in vector DB
db = FAISS.from_documents(documents, embeddings)

# LLM
llm = OpenAI(api_key=api_key)

# Chat loop
while True:
    query = input("\nAsk something (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    docs = db.similarity_search(query)

    response = llm.invoke(
        f"Answer this based on context: {docs[0].page_content} \n Question: {query}"
    )

    print("\nAnswer:", response)

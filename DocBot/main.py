from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

loader = PyPDFLoader(r"C:\Users\suriy\OneDrive\Documents\BlindSpotDetection[1]\BlindSpotDetection\Textbook.pdf")
documents = loader.load()

print(len(documents), "pages loaded")
print(documents[0].page_content[:500])

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

db = Chroma.from_documents(docs, embeddings)

retriever = db.as_retriever()

llm = Ollama(model="llama2")

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

query = "Explain the waterfall model"
response = qa_chain({"query": query})

print("Answer:", response["result"])
print("Source:", response["source_documents"][0].metadata)


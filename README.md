This project is a document chatbot built with LangChain
, ChromaDB
, and Ollama
It allows you to upload a PDF (e.g., a textbook) and then ask natural language questions about its contents.

 Features

Load and process large PDFs (e.g., 930 pages textbook).

Store document embeddings in a local ChromaDB vector database.

Use sentence-transformers for embeddings.

Query the document with Ollama’s Llama 2 / Mistral models.

Interactive Q&A chatbot experience.

🛠️ Installation
1. Clone the repository
git clone https://github.com/your-username/docbot.git
cd docbot

2. Create and activate virtual environment
python -m venv docbot_env
# On Windows (PowerShell)
.\docbot_env\Scripts\activate
# On Linux/Mac
source docbot_env/bin/activate

3. Install dependencies
pip install -r requirements.txt


If you don’t want to use a requirements.txt, install manually:

pip install langchain langchain-community langchain-core langchain-text-splitters
pip install langchain-huggingface langchain-ollama
pip install chromadb
pip install pypdf
pip install sentence-transformers sentencepiece

Ollama Setup

You need Ollama
 installed to run local LLMs like Llama 2 or Mistral.

Install Ollama → https://ollama.ai/download

in command prompt

Pull a model (example: Llama 2 7B):

ollama pull llama2:7b


or for Mistral (lighter & faster):

ollama pull mistral

 Usage

Run the chatbot:

python main.py


Sample interaction:

930 pages loaded
Enter your question: What is software engineering?
Answer: Software engineering is a systematic, disciplined, and quantifiable approach to software development and maintenance...

Project Structure
docbot/
│── main.py              # Main script for PDF Q&A
│── requirements.txt     # Dependencies
│── README.md            # Documentation
│── data/                # Your PDF files go here
│── docbot_env/          # Virtual environment (not pushed to GitHub)

Notes

First run may take time because Ollama downloads the model.

Large PDFs may take time to embed. Consider splitting them into smaller chunks.

Deprecation warnings from LangChain mean you should prefer langchain-huggingface and langchain-ollama imports.

Tested Versions

Python 3.12.0

langchain 0.3.27

langchain-community 0.3.29

langchain-huggingface 0.3.1

langchain-ollama 0.3.7

chromadb 1.0.20

pypdf 6.0.0

sentence-transformers 2.2.2

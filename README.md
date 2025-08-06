# 📄 SmartPDF QA Bot 🤖

An AI-powered chatbot that allows users to upload PDF documents and ask questions about their content. It leverages OpenAI's LLMs, semantic search with FAISS, and LangChain pipelines to provide intelligent, contextual answers.

---

## 🚀 Features

- 📤 Upload PDF documents
- 🧠 Extract and split document text into contextual chunks
- 🔍 Perform semantic search on document content
- 💬 Ask natural language questions about your document
- 🤖 Generate intelligent answers using GPT-3.5-turbo
- ⚡ Real-time web interface using Streamlit

---

## 🧱 Architecture Overview

```mermaid
flowchart LR
    A[User Uploads PDF] --> B[Text Extraction using PyPDF2]
    B --> C[Text Chunking - LangChain]
    C --> D[Generate Embeddings - OpenAI API]
    D --> E[Store Embeddings in FAISS Vector DB]
    F[User Question] --> G[Convert Query to Embedding]
    G --> H[Semantic Search in Vector DB]
    H --> I[Relevant Chunks]
    I --> J[Pass to GPT-3.5 via LangChain QA Chain]
    J --> K[Answer Generated]
    K --> L[Answer Displayed in Streamlit UI]


| Technology     | Purpose                               |
| -------------- | ------------------------------------- |
| **Python**     | Programming language                  |
| **Streamlit**  | Web app framework for UI              |
| **PyPDF2**     | PDF text extraction                   |
| **LangChain**  | LLM chains and embeddings pipeline    |
| **OpenAI API** | Embeddings + GPT-3.5-turbo (LLM)      |
| **FAISS**      | Vector store for fast semantic search |


├── chatbot.py                   # Main Streamlit app
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation


🧪 How It Works

1.PDF Upload: The user uploads a PDF via the Streamlit sidebar.

2.Text Extraction: PyPDF2 extracts text from each page.

3.Chunking: Text is split into overlapping chunks using LangChain’s RecursiveCharacterTextSplitter.

4.Embedding: Each chunk is converted into vector embeddings using OpenAI’s API.

5.Vector Store: Embeddings are stored in FAISS for similarity search.

6.User Query: The user types a question related to the document.

7.Semantic Search: The query is embedded and matched with relevant document chunks.

8.Answer Generation: Using GPT-3.5 and LangChain’s QA chain, a contextual answer is generated.

9.Display: The answer is shown in the Streamlit UI.




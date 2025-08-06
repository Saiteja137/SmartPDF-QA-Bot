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







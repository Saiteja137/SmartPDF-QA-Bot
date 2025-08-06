import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI



OPENAI_API_KEY = "Your Api Key" #openai key(pass your key here)

#Upload Pdf files
st.header("My First Chatbot")

with st.sidebar:
    st.title("Your Documnets")
    file = st.file_uploader("Upload a file and Start asking Questions",type="pdf")

#Extract the text
if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
        #st.write(text) it is used to display the text in the app, but we will not use it here.


#Break into Chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators = "\n",
        chunk_size = 1000,
        chunk_overlap = 150,
        length_function = len
    )

    chunks = text_splitter.split_text(text)
    #st.write(chunks) it is used to display the chunks in the app, but we will not use it here.



    #generating embeddings

    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)



    #create a vector store - FAISS(Facebook AI Similarity Search)

    vector_store = FAISS.from_texts(chunks,embeddings)

    """
    -Embeddings(openai) are used to convert text into numerical vectors.
    -FAISS is a library for efficient similarity search and clustering of dense vectors.
    -Vector store is a collection of vectors that can be used for similarity search.
    -FAISS is used to create a vector store from the chunks of text.
    """



    #get user question 
    user_question = st.text_input("Ask a question about the document")




    #do similarity search
    if user_question:
        match = vector_store.similarity_search(user_question)
        #st.write(match) # Display the matched chunks based on the user's question

        

        #define the LLM model
        llm = ChatOpenAI(
            openai_api_key=OPENAI_API_KEY,
            model_name="gpt-3.5-turbo",
            temperature=0,
            max_tokens=1000
        )


        #output results
        #chain -> take the question,get relevant document,pass it to the LLM and generate the result
        chain = load_qa_chain(llm,chain_type="stuff")
        response = chain.run(question=user_question, input_documents=match)
        st.write(response)  # Display the response from the LLM based on the user's question and matched documents
        #this answer will be coming from the document we uploaded not exact from the document because it is an generative model 
        # so it generates the answer based on the context of the document.

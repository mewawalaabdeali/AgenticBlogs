from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

class BlogContextBuilder:
    def __init__(self, transcript:str):
        self.transcript = transcript
        self.store = self._build_vectorstore()
        

    def _build_vectorstore(self):
        """Split the Transcript and builds a FAISS vector store with OpenAI Embeddings"""
        splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap=200)
        chunks = splitter.create_documents([self.transcript])

        embeddings = OpenAIEmbeddings(model='text-embedding-ada-002')
        vector_store = FAISS.from_documents(chunks, embeddings=embeddings)
        return vector_store
    
    
    
    def get_context(self, query:str, k:int=4)->str:
        """Retrieves top-k relevant chunks based on a query"""
        retriever = self.store.as_retriever(search_kwargs = {"k":k})
        documents = retriever.invoke(query)
        context = "\n\n".join([doc.page_content for doc in documents])
        return context
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

loader = PyPDFLoader("NOTES_Git.pdf")

docs = loader.load()

#print(len(docs))

#print(docs[0].page_content)

#print(docs[0].metadata)

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=10,  # 10,20 %
    separator=""
)


result = splitter.split_documents(docs)





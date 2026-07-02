from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import FAISS

# Create a simple document
content = """
Artificial Intelligence (AI) is transforming the way people work, learn, and communicate.
It enables computers to perform tasks that normally require human intelligence, such as
understanding language, recognizing images, and making decisions. AI is widely used in
healthcare, education, finance, transportation, and many other industries. As AI continues
to evolve, it offers exciting opportunities to solve complex problems, improve productivity,
and create innovative solutions. However, it is also important to use AI responsibly and
consider its ethical and social impacts.
"""

# Save the content to a text file
with open("langchain_intro.txt", "w", encoding="utf-8") as f:
    f.write(content)

# Load the document
loader = TextLoader("langchain_intro.txt", encoding="utf-8")
documents = loader.load()

print(f"Loaded {len(documents)} document(s)")

# Split the document into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
    separators=["\n\n", "\n", " ", ""]
)

chunks = text_splitter.split_documents(documents)

print(f"Split into {len(chunks)} chunks\n")

# Print each chunk
for i, chunk in enumerate(chunks, start=1):
    print(f"Chunk {i}:")
    print(chunk.page_content)
    print("-" * 50)
    
# create embedings
embeding_function = HuggingFaceBgeEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

print("create embeding and indexing in fiass")
db = FAISS.from_documents(documents=chunks, 
                          embedding=embeding_function)
print ("vector database create successfully")
print(f"store {len(chunks)} vectors in the database")
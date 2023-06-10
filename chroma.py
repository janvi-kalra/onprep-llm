import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./chroma_directory"
))

# chroma_client = chromadb.Client()

collection = client.create_collection(name="my_collection")
# collection = client.get_collection(name="my_collection")

k = 5
id = 1

# Adds private content to Chroma
def addToCollection(text, source):
    global id  

    collection.add(
        documents=[text],
        metadatas=[{"source": source}],
        ids=[str(id)]
    )
    id += 1

# Chooses K-most relevant diary entries
def getRelevantResponses(query):
    results = collection.query(
        query_texts=[query],
        n_results=k
    )
    print(results)
    return results
import chromadb
from chromadb.config import Settings
import string
import random

client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./chroma_directory"
))

try:
    client.create_collection(name="my_collection")
except:
    collection = client.get_collection(name="my_collection")

k = 5

def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(letters_and_digits) for _ in range(length))
    return random_string

# Adds private content to Chroma
def addToCollection(text, source):
    short_text = text.split("Journal Entry")
    for t in short_text: 
        collection.add(
            documents=[t],
            metadatas=[{"source": source}],
            ids=[generate_random_string(10)]
        )
        # print('added to collection: ', t)

# Chooses K-most relevant diary entries
def getRelevantResponses(query):
    results = collection.query(
        query_texts=[query],
        n_results=k
    )
    # print('query', query)
    # print('relevant results', results)
    return results
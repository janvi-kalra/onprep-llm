import chromadb
from chromadb.config import Settings
import string
import random

client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./chroma_directory"
))

# chroma_client = chromadb.Client()

# collection = client.create_collection(name="my_collection")
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
    collection.add(
        documents=[text],
        metadatas=[{"source": source}],
        ids=[generate_random_string(10)]
    )

# Chooses K-most relevant diary entries
def getRelevantResponses(query):
    results = collection.query(
        query_texts=[query],
        n_results=k
    )
    print(results)
    return results




# import chromadb
# from chromadb.config import Settings
#
# class ChromaClient:
#     def __init__(self):
#         self.k = 5
#         self.id = 1
#         self.client = chromadb.Client(Settings(
#             chroma_db_impl="duckdb+parquet",
#             persist_directory="./chroma_directory"
#         ))
#         try:
#             self.client.create_collection(name="my_collection")
#         except ValueError as e:
#             # collection already exists
#             pass
#         self.collection = self.client.get_collection(name="my_collection")
#
#         # Adds private content to Chroma
#     def addToCollection(self, text, source):
#         global id
#
#         self.collection.add(
#             documents=[text],
#             metadatas=[{"source": source}],
#             ids=[str(id)]
#         )
#         id += 1
#
#     # Chooses K-most relevant diary entries
#     def getRelevantResponses(self, query):
#         results = self.collection.query(
#             query_texts=[query],
#             n_results=k
#         )
#         print(results)
#         return results
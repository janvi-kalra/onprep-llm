# https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
# responsible for turning text -> embeddings
# did not end up using, because chroma handles embeddings.

from sentence_transformers import SentenceTransformer

# load the model before running the function, so that we don't need to load the model every time 
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def embed_list(paragraph_list):
    # sentences = ["This is an example sentence", "Each sentence is converted"]
    embeddings = model.encode(paragraph_list)
    return embeddings

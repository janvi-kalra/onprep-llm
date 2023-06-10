# https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
# responsible for turning text -> embeddings

from sentence_transformers import SentenceTransformer

def test(sentences):
    # sentences = ["This is an example sentence", "Each sentence is converted"]
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings = model.encode(sentences)
    return embeddings

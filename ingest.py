
from .embed import embed_list 


def get_paragraphs_for_file(file_path)):
    with open(file_path, 'r') as file:
        text = file.read()

    paragraphs = text.split('\n\n')
    return paragraphs

def upsert_embeddings_to_chroma():  #TODO 
    return False 

def ingest_file_to_chroma(file_path): 
    text_paragraphs = get_paragraphs_for_file(file_path)
    embeddings = embed_list(text_paragraphs)
    upsert_result = upsert_embeddings_to_chroma(embeddings)
    # TODO: ingest embeddings into chroma
    return {
        'upsert_result': upsert_result, 
        'paragraphs': text_paragraphs
    }

# Example usage
file_path = 'path/to/your/file.txt'
paragraphs = ingest_file_to_chroma(file_path)
print(paragraphs)


from .embed import embed_list 

####################################
## HELPERS 
####################################

### Future Versions: once past MVP 
# import nltk.data
# tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# def extract_paragraphs_from_text_nltk(text, segment_length=3):
#     sentences = tokenizer.tokenize(text)
#     segments = [sentences[i:i+segment_length] for i in range(0, len(sentences), segment_length)]
#     return segments

def extract_paragraphs_from_text(text):
    """Super lightweight text splitter. 
    Splits the text into segments based on new paragraphs, or every 1000 characters at the nearest ',' or '.'. 

    Future versions: Use 'nltk' library (which requires downloading packages into the repo, which can add dependencies for hosting; can add post-hackathon). 
    """
    segments = []
    current_segment = ''

    paragraphs = text.split('\n\n')
    for paragraph in paragraphs:
        sentences = paragraph.split('.')
        for sentence in sentences:
            if len(current_segment) + len(sentence) <= 1000:
                current_segment += sentence + '.'
            else:
                segments.append(current_segment)
                current_segment = sentence + '.'

    if current_segment:
        segments.append(current_segment)

    return segments

def upsert_embeddings_to_chroma():  #TODO 
    return False 


def load_text_from_file(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    return text

####################################
## MAIN 
####################################

def ingest_file_to_chroma(file_path): 
    raw_text = load_text_from_file(file_path)
    text_paragraphs = extract_paragraphs_from_text(raw_text)
    embeddings = embed_list(text_paragraphs)
    upsert_result = upsert_embeddings_to_chroma(embeddings)
    # TODO: ingest embeddings into chroma
    return {
        'upsert_result': upsert_result, 
        'paragraphs': text_paragraphs
    }

## Example usage
file_path = 'path/to/your/file.txt'
paragraphs = ingest_file_to_chroma(file_path)
print(paragraphs)

# from llama_index import download_loader

# GmailReader = download_loader('GmailReader')
# loader = GmailReader(query="from: me label:inbox")
# documents = loader.load_data()
# print(documents)

from llama_index import download_loader
import re

GoogleDocsReader = download_loader('GoogleDocsReader')

# gdoc_ids = ['1wf-y2pd9C878Oh-FmLH7Q_BQkljdm6TQal-c1pUfrec']
# loader = GoogleDocsReader()
# documents = loader.load_data(document_ids=gdoc_ids)
# print(documents)

def inputGoogleDoc(link):
    doc_id = re.search(r"/d/([a-zA-Z0-9-_]+)", link).group(1)
    print('the doc_id', doc_id)
    GoogleDocsReader = download_loader('GoogleDocsReader')
    gdoc_ids = [doc_id]
    loader = GoogleDocsReader()
    documents = loader.load_data(document_ids=gdoc_ids)
    documents[0]
    print('text', text)
    return text
    
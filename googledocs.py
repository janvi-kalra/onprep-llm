# FOR GETTING FROM GMAIL: 
# GmailReader = download_loader('GmailReader')
# loader = GmailReader(query="from: me label:inbox")
# documents = loader.load_data()
# print(documents)

from llama_index import download_loader
import re

GoogleDocsReader = download_loader('GoogleDocsReader')

def getContent(link):
    doc_id = re.search(r"/d/([a-zA-Z0-9-_]+)", link).group(1)
    print('the doc_id', doc_id)
    GoogleDocsReader = download_loader('GoogleDocsReader')
    gdoc_ids = [doc_id]
    loader = GoogleDocsReader()
    documents = loader.load_data(document_ids=gdoc_ids)
    return documents[0].text

    
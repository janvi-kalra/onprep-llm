import chroma
import googledocs
from chroma import getRelevantResponses
from query import get_completion_from_openassistant

### Ingest 
google_link = 'https://docs.google.com/document/d/1-aLy3QMjoB2Ssr46m27gvTpfxfe9mj2865Gplwu16W8/edit'
input_data = googledocs.getContent(google_link)

chroma.addToCollection(input_data, 'none')
# run_query('LLM')
query = 'LLM'
resp = getRelevantResponses(query)
completion = get_completion_from_openassistant(query, resp['documents'])
import pdb; pdb.set_trace()


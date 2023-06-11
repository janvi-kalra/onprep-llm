# import requests
#
# API_URL = "https://api-inference.huggingface.co/models/OpenAssistant/falcon-7b-sft-top1-696"
# API_TOKEN = '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'
# headers = {"Authorization": f"Bearer {API_TOKEN}"}
#
# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.json()
#
# output = query({
#     "inputs": "Can you please let us know more details about your ",
# })

# import openai
# OPENAI_API_KEY = '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'
# openai.api_key = OPENAI_API_KEY
#
# resp = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Who won the world series in 2020?"},
#         {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#         {"role": "user", "content": "Where was it played?"}
#     ]
# )
import chroma
import googledocs
from chroma import getRelevantResponses
from query import run_query, get_completion_from_openassistant

### Ingest 
google_link = 'https://docs.google.com/document/d/1ukOID1wlstzmE1kC8CMZkiz-zDrgOtCNtgcdHXg7vZg/edit'
input_data = googledocs.getContent(google_link)
# Process the input_data with your Python code here
chroma.addToCollection(input_data, 'none')

### Query 
# run_query('LLM')
query = 'LLM'
resp = getRelevantResponses(query)
completion = get_completion_from_openassistant(query, resp['documents'])
import pdb; pdb.set_trace()



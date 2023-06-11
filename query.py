from typing import List

from chroma import getRelevantResponses
from embed import embed_list
import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

####################################
## HELPERS 
####################################
def format_query_system_context(relevant_retrievals: List[str]) -> str:
    """Format system-level prompt for the user"""
    context = ' '.join([r[0] for r in relevant_retrievals])
    return f'You are an expert IFS Therapist, and you are helping someone process their memories. ' \
           f'Here are some relevant memories from the person’s journal. ' \
           f'Please use this context to help them answer their questions: ' \
           f'{context} ' \

# TODO 
def get_completion_from_openassistant(query: str, relevant_retrievals: List[str]) -> str:
    """Get the completion from OpenAssistant. 
    """
    syste_context = format_query_system_context(relevant_retrievals)
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": syste_context},
            {"role": "user", "content": query},
        ]
    )
    completion = resp['choices'][0]['message']['content']
    return completion


####################################
## MAIN 
####################################
def run_query(query:str) -> dict: 
    """Run a query against the Chroma API 
    """
    # query_embed = embed_list([query])
    relevant_retrievals = getRelevantResponses(query)
    import pdb; pdb.set_trace()
    completion = get_completion_from_openassistant(query, relevant_retrievals)
    return completion






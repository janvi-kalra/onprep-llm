
from .embed import embed_list

####################################
## HELPERS 
####################################

# TODO 
def retrieve_from_chroma(embedded_query:list) -> dict:
    """Retrieve the embedded text from Chroma. 
    """
    return False 

def get_retrievals(query:str) -> dict:
    embedded_query = embed_list(query)
    relevant_retrievals = retrieve_from_chroma(embedded_query)
    return relevant_retrievals

# TODO 
def format_prompt(query:str, relevant_retrievals:dict) -> str:
    """Format the prompt for the user. 
    """
    return False

# TODO 
def get_completion_from_openassistant(prompt:str) -> str:
    """Get the completion from OpenAssistant. 
    """
    return False

####################################
## MAIN 
####################################

def run_query(query:str) -> dict: 
    """Run a query against the Chroma API 
    """
    query_embed = embed_list([query])
    relevant_retrievals = retrieve_from_chroma(query_embed)
    prompt = format_prompt(query, relevant_retrievals)
    completion = get_completion_from_openassistant(prompt)
    return completion






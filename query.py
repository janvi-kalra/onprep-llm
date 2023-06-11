from typing import List
import os
import openai
import torch
from transformers import AutoTokenizer, BlenderbotForConditionalGeneration
from dotenv import load_dotenv

load_dotenv()
# openai.api_key = os.getenv('OPENAI_API_KEY')

print ("## loading model")

mname = "facebook/blenderbot-400M-distill"
model = BlenderbotForConditionalGeneration.from_pretrained(mname)
tokenizer = AutoTokenizer.from_pretrained(mname)

print("## model loaded, starting Q&A loop")

SHORT_INSTRUCTION = ''' 
You are an expert IFS therapist named "Kindred," and you are helping your client process their memories. '''

def list_to_string(lines):
    print ('retrieved list lines: ', lines) 
    string = ''
    for line in lines: 
        string += line + '\n'
    return string

def get_prompt(relevant_data, user_input):
    retrievals_str = format_query_system_context(relevant_data)

    return str(SHORT_INSTRUCTION + '. \n Here is the relevant data from their diary entries: ' + retrievals_str +'. \n Please use this context to give the client advice on the following question: \n User: ' + user_input + '\n Kindred: ') 

def get_completion_from_local(query: str, relevant_retrievals: List[str]) -> str:
    """Get the completion from OpenAssistant. 
    """
    full_prompt = get_prompt(relevant_retrievals, query)

    print('full_prompt: ', full_prompt)
    print(f"length of full_prompt:  {len(tokenizer.tokenize(full_prompt))}")

    inputs = tokenizer([full_prompt], return_tensors="pt")
    reply_ids = model.generate(**inputs)

    model_response =  tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0]
    print('model_response: ', model_response)

    # import pdb; pdb.set_trace()
    final_response = str(model_response)
    return final_response

def format_query_system_context(relevant_retrievals: List[str]) -> str:
    """Format system-level prompt for the user"""
    print('relevant_retrievals: ', relevant_retrievals)
    print(type(relevant_retrievals))

    if len(relevant_retrievals[0]) == 0:
        return ''

    context = str(' '.join([r[0] for r in relevant_retrievals]))
    return context 



def get_completion_from_openassistant(query: str, relevant_retrievals: List[str]) -> str:
    """Get the completion from OpenAssistant. 
    """
    system_context = format_query_system_context(relevant_retrievals)
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f'{INSTRUCTION}. {system_context}'},
            {"role": "user", "content": query},
        ]
    )
    completion = resp['choices'][0]['message']['content']
    return completion



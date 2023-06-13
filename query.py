from typing import List
import os
# import openai
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


def list_to_string(lines):
    # print ('retrieved list lines: ', lines) 
    string = ''
    for line in lines: 
        string += line + '\n'
    return string

def get_prompt(relevant_data, user_input):
    retrievals_str = format_query_system_context(relevant_data)
    # print('retrievals_str', retrievals_str); 

    return str('A person has the following diary entries: ' + retrievals_str +'. \n Based on those diary entries, answer the following question: ' + user_input ) 

def get_completion_from_local(query: str, relevant_retrievals: List[str]) -> str:
    """Get the completion from local model. 
    """
    full_prompt = get_prompt(relevant_retrievals, query)

    print(f"full_prompt: \n {full_prompt}\n")
    # print(f"length of full_prompt:  {len(tokenizer.tokenize(full_prompt))}\n")

    if (len(tokenizer.tokenize(full_prompt)) > 128): 
            midpoint = len(full_prompt) // 2
            full_prompt = full_prompt[:midpoint]

    inputs = tokenizer([full_prompt], return_tensors="pt")
    reply_ids = model.generate(**inputs)

    model_response =  tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0]
    # print('model_response: ', model_response)

    # import pdb; pdb.set_trace()
    final_response = str(model_response)
    return final_response

def format_query_system_context(relevant_retrievals: List[str]) -> str:
    """Format system-level prompt for the user"""
    if len(relevant_retrievals[0]) == 0:
        return ''

    context = str(' '.join([r[0] for r in relevant_retrievals]))
    return context 


def get_completion_from_chatgpt(query: str, relevant_retrievals: List[str]) -> str:
    """Get the completion from ChatGPT. 
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



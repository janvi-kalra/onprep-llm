from typing import List
from transformers import AutoTokenizer, BlenderbotForConditionalGeneration
import torch

import os
import openai
from dotenv import load_dotenv

load_dotenv()
# openai.api_key = os.getenv('OPENAI_API_KEY')

print ("## loading model")

mname = "facebook/blenderbot-400M-distill"
model = BlenderbotForConditionalGeneration.from_pretrained(mname)
tokenizer = AutoTokenizer.from_pretrained(mname)
# UTTERANCE = "My friends are cool but they eat too many carbs."

print("## model loaded, starting Q&A loop")

SHORT_INSTRUCTION = ''' 
You are an expert IFS therapist named "Kindred," and you are helping your client process their memories. '''

def get_prompt(relevant_data, user_input):
    return str(SHORT_INSTRUCTION + '. \n Here is the relevant data from their diary entries: ' + relevant_data +'. \n Please use this context to give the client advice on the following question: \n User: ' + user_input + '\n Kindred: ') 

def get_completion_from_local(query: str, relevant_retrievals: List[str]) -> str:
    """Get the completion from OpenAssistant. 
    """
    full_prompt = get_prompt(relevant_retrievals, query)
    inputs = tokenizer([full_prompt], return_tensors="pt")
    reply_ids = model.generate(**inputs)
    model_response = str("Kindred: ", tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0])
    return model_response

def format_query_system_context(relevant_retrievals: List[str]) -> str:
    """Format system-level prompt for the user"""
    context = ' '.join([r[0] for r in relevant_retrievals])
    return f'Here are some relevant memories from the person’s journal. ' \
           f'Please use this context to help them answer their questions: ' \
           f'{context} '


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



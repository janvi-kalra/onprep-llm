from transformers import AutoTokenizer, BlenderbotForConditionalGeneration

from prompt import INSTRUCTION as INSTRUCTION

import torch

print ("## loading model")

mname = "facebook/blenderbot-400M-distill"
model = BlenderbotForConditionalGeneration.from_pretrained(mname)
tokenizer = AutoTokenizer.from_pretrained(mname)
# UTTERANCE = "My friends are cool but they eat too many carbs."

print("## model loaded, starting Q&A loop")


# Let's chat for 5 lines
for step in range(30):
    user_input = str(INSTRUCTION + CONTEXT + input(">> Client:"))
    # encode the new user input, add the eos_token and return a tensor in Pytorch
    # new_user_input_ids = tokenizer.encode( + tokenizer.eos_token, return_tensors='pt')

    inputs = tokenizer([user_input], return_tensors="pt")
    reply_ids = model.generate(**inputs)
    print("Bot: ", tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0])

from transformers import AutoTokenizer, BlenderbotForConditionalGeneration

from prompt import INSTRUCTION as INSTRUCTION

import torch

print ("## loading model")

mname = "facebook/blenderbot-400M-distill"
model = BlenderbotForConditionalGeneration.from_pretrained(mname)
tokenizer = AutoTokenizer.from_pretrained(mname)
# UTTERANCE = "My friends are cool but they eat too many carbs."

print("## model loaded, starting Q&A loop")

CONTEXT = """ 

==== 
Here is some relevant context from the client's past journal entries: 

Dear Diary,
Today marks the beginning of a new chapter in my life. I arrived in San Francisco, and I must admit, I'm feeling overwhelmed. The city is vast, bustling, and unfamiliar. I can't help but feel a knot of anxiety tightening in my stomach. What if I don't fit in here? What if I can't find my place? The memory of that incident last year still haunts me, weighing heavily on my conscience. I hope this new city will offer me a fresh start and a chance to heal.
Journal Entry 2:

Dear Diary,
I ventured out today to explore the city. The streets of San Francisco are lined with beautiful Victorian houses, each with its unique charm. It's a stark contrast to the modern, glass-and-steel skyline. Despite the beauty, I can't shake off the feeling of unease. The incident from last year keeps playing over and over in my mind. Will I ever be able to move on and forgive myself?

==== 

Please use this journal context to help your client answer their question: 

"""


# Let's chat for 5 lines
for step in range(30):
    user_input = str(INSTRUCTION + CONTEXT + input(">> Client:"))
    # encode the new user input, add the eos_token and return a tensor in Pytorch
    # new_user_input_ids = tokenizer.encode( + tokenizer.eos_token, return_tensors='pt')

    inputs = tokenizer([user_input], return_tensors="pt")
    reply_ids = model.generate(**inputs)
    print("Bot: ", tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0])

# https://huggingface.co/OpenAssistant/falcon-7b-sft-top1-696

from transformers import AutoTokenizer
import transformers
import torch

model = "OpenAssistant/falcon-7b-sft-top1-696"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
)

input_text="<|prompter|>What is a meme, and what's the history behind this word?<|endoftext|><|assistant|>"

sequences = pipeline(
    input_text,
    max_length=500,
    do_sample=True,
    return_full_text=False,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")
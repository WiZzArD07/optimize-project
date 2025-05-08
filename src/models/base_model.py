# src/models/base_model.py

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class BaseLLM:
    def __init__(self, model_name="gpt2"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.model.eval()

    def generate(self, prompt, max_tokens=100):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_tokens,
                do_sample=True,
                temperature=0.7
            )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example:
# llm = BaseLLM()
# print(llm.generate("What is the capital of France?"))

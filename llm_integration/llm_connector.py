import transformers

class LLMConnector:
    def __init__(self):
        self.model = transformers.AutoModelForCausalLM.from_pretrained("gpt2")
        self.tokenizer = transformers.AutoTokenizer.from_pretrained("gpt2")

    def generate_text(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=100)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
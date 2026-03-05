class PromptEngine:
    def __init__(self):
        self.base_prompt = "Write a creative story about:" 

    def create_prompt(self, topic):
        return self.base_prompt + topic
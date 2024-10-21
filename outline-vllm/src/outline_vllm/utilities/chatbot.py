from outlines import generate
from loadModel import model
from agents.reactAgent import regex_str

class ChatBot:
    def __init__(self, prompt=""):
        self.prompt = prompt

    def __call__(self, user_prompt):
        self.prompt += user_prompt
        result = self.execute()
        return result

    def execute(self):
        generator = generate.regex(model, regex_str)
        result = generator(self.prompt, max_tokens=1024, temperature=0, seed=42)
        return result
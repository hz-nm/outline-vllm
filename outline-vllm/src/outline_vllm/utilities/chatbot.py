from outlines import generate
from loadModel import loadLlamaModel
from agents.pydanticModels import Decision
from outlines.integrations.utils import convert_json_schema_to_str
from outlines.fsm.json_schema import build_regex_from_schema

json_schema = Decision.model_json_schema()
schema_str = convert_json_schema_to_str(json_schema=json_schema)
regex_str = build_regex_from_schema(schema_str)

model = loadLlamaModel()


class ChatBot:
    def __init__(self, prompt="", model=loadLlamaModel()):
        self.prompt = prompt
        self.model = model

    def __call__(self, user_prompt):
        self.prompt += user_prompt
        result = self.execute()
        return result

    def execute(self):
        generator = generate.regex(model, regex_str)
        result = generator(self.prompt, max_tokens=1024, temperature=0, seed=42)
        return result

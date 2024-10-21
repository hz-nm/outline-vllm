import httpx
from enum import Enum
from pydantic import BaseModel, Field
from typing import Union
from outlines.integrations.utils import convert_json_schema_to_str
from outlines.fsm.json_schema import build_regex_from_schema


def wikipedia(q):
    return httpx.get("https://en.wikipedia.org/w/api.php", params={
        "action": "query",
        "list": "search",
        "srsearch": q,
        "format": "json"
    }).json()["query"]["search"][0]["snippet"]


def calculate(numexp):
    return eval(numexp)


class Action(str, Enum):
    wikipedia = "wikipedia"
    calculate = "calculate"
    

class ReasonAndAct(BaseModel):
    Scratchpad: str = Field(..., description="Information from the Observation useful to answer the question")
    Thought: str = Field(..., description="It describes your thoughts about the question you have been asked")
    Action: Action
    Action_Input: str = Field(..., description="The arguments of the Action.")
    
class FinalAnswer(BaseModel):
    Scratchpad: str = Field(..., description="Information from the Observation useful to answer the question")
    Final_Answer: str = Field(..., description="Answer to the question grounded on the Observation")
    

class Decision(BaseModel):
    Decision: Union[ReasonAndAct, FinalAnswer]
    

def getRegexSchema():
    json_schema = Decision.model_json_schema()
    schema_str = convert_json_schema_to_str(json_schema=json_schema)
    regex_str = build_regex_from_schema(schema_str)
    print(regex_str)
    # '\\{[ ]?"Decision"[ ]?:[ ]?(\\{[ ]?"Scratchpad"[ ]?:[ ]?"([^"\\\\\\x00-\\x1F\\x7F-\\x9F]|\\\\["\\\\])*"[ ]?,[ ]?"Thought"[ ]?:[ ]?"([^"\\\\\\x00-\\x1F\\x7F-\\x9F]|\\\\["\\\\])*"[ ]?,[ ]?"Action"[ ]?:[ ]?("wikipedia"|"calculate")[ ]?,[ ]?"Action_Input"[ ]?:[ ]?"([^"\\\\\\x00-\\x1F\\x7F-\\x9F]|\\\\["\\\\])*"[ ]?\\}|\\{[ ]?"Scratchpad"[ ]?:[ ]?"([^"\\\\\\x00-\\x1F\\x7F-\\x9F]|\\\\["\\\\])*"[ ]?,[ ]?"Final_Answer"[ ]?:[ ]?"([^"\\\\\\x00-\\x1F\\x7F-\\x9F]|\\\\["\\\\])*"[ ]?\\})[ ]?\\}'
    
    

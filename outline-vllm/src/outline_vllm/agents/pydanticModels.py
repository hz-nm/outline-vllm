from pydantic import BaseModel, Field
from typing import Union
from enum import Enum


class Action(str, Enum):
    wikipedia = "wikipedia"
    calculate = "calculate"


class ReasonAndAct(BaseModel):
    Scratchpad: str = Field(
        ...,
        description="Information from the Observation useful to answer the question",
    )
    Thought: str = Field(
        ...,
        description="It describes your thoughts about the question you have been asked",
    )
    Action: Action
    Action_Input: str = Field(..., description="The arguments of the Action.")


class FinalAnswer(BaseModel):
    Scratchpad: str = Field(
        ...,
        description="Information from the Observation useful to answer the question",
    )
    Final_Answer: str = Field(
        ..., description="Answer to the question grounded on the Observation"
    )


class Decision(BaseModel):
    Decision: Union[ReasonAndAct, FinalAnswer]


class ReActQuery(BaseModel):
    query: str

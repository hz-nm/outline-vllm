from utilities.loadModel import loadLlamaModel
from fastapi import FastAPI
from agents.queryFunction import query
from agents.pydanticModels import ReActQuery
from utilities.chatbot import ChatBot

# TODO do something with Fast API to create an endpoint
model = loadLlamaModel()

app = FastAPI()


@app.post("/react_agent")
async def reActAgent(request: ReActQuery):
    userQuery = request.query
    response = query(question=userQuery, chatbot=ChatBot)

    return response

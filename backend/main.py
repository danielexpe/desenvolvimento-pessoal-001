from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Goal(BaseModel):
    title: str
    description: str

@app.post("/goals/")
async def create_goal(goal: Goal):
    return goal

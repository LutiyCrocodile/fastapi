import uvicorn
from fastapi import FastAPI
from models import Feedback

app = FastAPI()


all_ = []


@app.post("/feedback")
async def get_feedback(feedback: Feedback):
    all_.append(feedback)
    return {"message":f"Feedback received. Thank you, {feedback.name}!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
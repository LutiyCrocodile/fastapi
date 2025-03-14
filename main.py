import uvicorn
from fastapi import FastAPI
from models import UserCreate

app = FastAPI()

try:
    @app.post("/create_user")
    async def create_user(user: UserCreate):
        return {
            "name": user.name,
            "email": user.email,
            "age": user.age,
            "is_subscribed": user.is_subscribed
        }


except Exception as e:
    print("[INFO] Error ", e)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
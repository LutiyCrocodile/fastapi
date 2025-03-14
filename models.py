from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int = Field(gt=0, le=100)
    is_subscribed: bool
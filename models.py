from pydantic import BaseModel, EmailStr, Field

class Product(BaseModel):
    product_id: int = Field(ge=0)
    name: str
    category: str
    price: float
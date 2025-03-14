import uvicorn
from fastapi import FastAPI
from models import Product

app = FastAPI()

sample_product_1 = {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99
}

sample_product_2 = {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99
}

sample_product_3 = {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99
}

sample_product_4 = {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99
}

sample_product_5 = {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99
}

sample_products = [sample_product_1, sample_product_2, sample_product_3, sample_product_4, sample_product_5]


@app.get("/product/{product_id}")
async def detail_product(product_id: int) :
    product = [item for item in sample_products if item['product_id'] == product_id]
    if product:
        return product[0]
    return {"message": "404 NOT_FOUND"}


@app.get("/products/search")
def get_product(keyword: str, category: str = None, limit: int = 10):
    products = []
    for product in sample_products:
        if keyword.lower() in product['name'].lower():
            products.append(product)
    if category:
        products = list(filter(lambda item: item["category"] == category, products))
    return products[:limit]


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
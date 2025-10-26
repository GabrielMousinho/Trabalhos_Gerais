from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

import os
import requests

load_dotenv()
from deta import Deta  # Import Deta

DETA_PROJECT_KEY = Deta(os.environ["e0shRVSduBQg_4R66anxdFfm8o7V46VbPnLT5H8RBah6W"])

db = deta.Base("products")

app = FastAPI()

class Products(BaseModel):
    name: str

class Categories(BaseModel):
    name: str

@app.post("/products")
async def create_product(product: Products):
    new_product = db.insert(product.dict())

    return new_product

@app.get("/products")
async def get_products():
    res = db.fetch()
    all_items = res.items

    while res.last:
        res = db.fetch(last=res.last)
        all_items += res.items

    return all_items

@app.get("/products/{id}")
async def get_product_by_id(id: str):
    product = db.get(id)

    if product:
        return product

    raise HTTPException(status_code=404, detail="Product not found.")

@app.put("/products/{product_id}")
async def update_product(id: str, product: Products):
    db.update(product.dict(), id)

    return product

@app.delete("/products/{product_id}")
async def delete_product(id: str):
    db.delete(id)

    return {"detail": "Removed successully."}

@app.post("/categories")
async def create_category(category: Categories):
    new_category = db.insert(product.dict())

    return new_category

@app.get("/categories")
async def get_categories():
    res = db.fetch()
    all_items = res.items

    while res.last:
        res = db.fetch(last=res.last)
        all_items += res.items

    return all_items

@app.get("/categories/{id}")
async def get_category_by_id(id: str):
    category = db.get(id)

    if category:
        return category

    raise HTTPException(status_code=404, detail="Category not found.")

@app.put("/categories/{category_id}")
async def update_category(id: str, category: Categories):
    db.update(category.dict(), id)

    return category

@app.delete("/categories/{category_id}")
async def delete_category(id: str):
    db.delete(id)

    return {"detail": "Removed successully."}

@app.put("/products/{product_id}/categories")
async def update_product_categories(id: str, product: Products, category: Categories):
    db.update(product.dict(), id)

    return product

@app.delete("/products/{product_id}/categories")
async def delete_product_categories(id: str, category: Categories):
    db.delete(category.dict(), id)

    return {"detail": "Removed successully."}

@app.get("/categories/{category_id}/products")
async def get_product_by_category(id: str):
    category = db.get(product)

    if category:
        return product

    raise HTTPException(status_code=404, detail="Category not found.")

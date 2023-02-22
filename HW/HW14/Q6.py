from __future__ import annotations
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    name: str
    price: float
    quantity: int

app = FastAPI()
items = [
    {'id': 1, 'name': 'apple', 'quantity': 2, 'price': 3.25},
    {'id': 2, 'name': 'banana', 'quantity': 5, 'price': 10.2},
    {'id': 3, 'name': 'carrot', 'quantity': 10, 'price': 2},
    {'id': 4, 'name': 'durian', 'quantity': 6, 'price': 4.5},
]

@app.post('/total_price/')
def sum_of_items(item: List[Item]):
    total_price = 0
    for item in items:
        total_price += item.price * item.quantity
    return {'total_price': total_price}
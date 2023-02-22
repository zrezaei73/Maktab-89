from __future__ import annotations

from typing import List

from fastapi import FastAPI

app = FastAPI()

#
# @app.get('/search/')
# def search_term(term: str = None):
#     try:
#         with open('Q1/term.txt', 'r') as f:
#             lines = f.readlines()
#             result = [line for line in lines if q.lower() in line.lower()]
#             return result
#     except:
#         return 'Error: could not open file!'



db = [
    {'id': 1, 'name': 'apple', 'description': 'a sweet fruit'},
    {'id': 2, 'name': 'banana', 'description': 'a yellow fruit'},
    {'id': 3, 'name': 'carrot', 'description': 'an orange vegetable'},
    {'id': 4, 'name': 'durian', 'description': 'a spiky fruit'},
]
@app.get('/items/')
def search_items(q: str = None):
    if not q:
        return term
    result = [item for item in db if q.lower() in term['name'].lower() or q.lower() in term['description'].lower()]
    return result
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Blog(BaseModel):
    title:str
    body: str
    published : Optional[bool]


@app.get('/')
def index():
    return {'data': 'blog list'}


@app.get('/blog/published')
def show():
    return {'published data'}


@app.get('/blog/{id}')
def show(id:int):
    return {'data': id}


@app.post('/blog')
def add_blog(request:Blog):
    return {"data": f"blog created with title as {request.title} and content is {request.body}"}

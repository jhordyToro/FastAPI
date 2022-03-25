#Python
from lib2to3.pytree import Node
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body

app = FastAPI()

class Person(BaseModel):
    first_name: str
    last_name: str 
    age: int
    hair_color: Optional[str] = None
    married: Optional[bool] = None

@app.get('/')
def home():
    return 'hola :3'

@app.post('/person/new')
def persona(person: Person = Body(...)):
    return person

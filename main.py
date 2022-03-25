#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body,Query

app = FastAPI()
class persona(BaseModel):
    first_name: str 
    last_name: str
    age: int
    hair_color: Optional[str] = None
    married: Optional[str] = None

@app.get('/')
def home():
    return 'hola xd'

#Request and response Body

@app.post('/person/new')
def people(person: persona = Body(...)):
    return person

#Validaciones: Query parameters

@app.get('/person/deatils')
def details(
    name: Optional[str] = Query(None,min_length=1,max_length=50),
    age: Optional[str] = Query(None,min_length=1,max_length=3)
):
    return {name: age}


#Python
from importlib.resources import path
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body,Query,Path

app = FastAPI()

class located(BaseModel):
    city: str
    adress: str 
    countri: str

class persona(BaseModel):
    first_name: str 
    last_name: str
    age: int
    hair_color: Optional[str] = None
    married: Optional[bool] = None

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
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title='person name',
        description="person name, needs a value greater than 0 and less than 50"
    ),
    age: Optional[int] = Query(
        ...,
        gt=0,
        it=1000)
):
    return {name: age}

#Validaciones: Path parameters
@app.get('/person/details/{person_id}')
def details(
    person_id: int = Path(
        ...,
        gt=0,
        title='person id',
        description='person id, the value must be greater than 0'
        )
):
    return {person_id: 'if it exists'}

#validaciones: request Body
@app.put('/person/{person_id}')
def update_person(
    person_id: int = Path(
        ...,
        gt=0,
        title='person ID',
        description='this is the person ID'
        ),
    person: persona = Body(...),
    located: located = Body(...)
    ):
    result = person.dict()
    result.update(located.dict())
    return result
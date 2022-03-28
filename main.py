#Python
from typing import Optional #esta libreria nos permite hacer un valor Optional valga la redundancia
from enum import Enum #Esta libreria nos permite enumerar o determinar valores predeterminados

#Pydantic
from pydantic import BaseModel #esta libreria nos permite generar una base de un modelo por ejemplo located y persona
from pydantic import Field # Field nos permite ponerle parametros a al Body los paametros son iguales pero se importa desde pydantic
from pydantic import EmailStr,HttpUrl,NegativeFloat,PositiveFloat

#FastAPI
from fastapi import FastAPI #importamos FastAPI desde fastapi XD
from fastapi import Body,Query,Path #el Query es para las Opcionales, el Path son para las variables del URL (asi no se llama pero pa identificarlas) y body en este caso es solo para definir si es requerido o no en las otras tambien se puede pero es mala practica
#los Requests Body son para enviar información que tiene formato de un modelo


app = FastAPI()

class enum(Enum): # asi :3
    white = 'white'
    brown = 'brown'
    black = 'black'
    blonde = 'blonde'
    red = 'red'


class located(BaseModel):
    city: str = Field(...,min_length=1,max_length=50,example='cartagena')
    adress: str = Field(...,min_length=1,max_length=50,example='74A - 31i')
    countri: str = Field(...,min_length=1,max_length=25,example='colombia')
    Email: EmailStr 
    Url: HttpUrl 
    float_positive: PositiveFloat 
    float_negative: NegativeFloat 



class persona(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example='jhordy'    
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example='Toro Arroyo'
    )
    age: int = Field(
        ...,
        gt=0,
        it=115,
        example=17
    )
    hair_color: Optional[enum] = Field(default=None,example='black')
    married: Optional[bool] = Field(default=None,example=False)
    
    # class Config:
    #     schema_extra = {
    #         'example': {
    #             'first_name': 'Jhordy',
    #             'last_name': 'Toro Arroyo',
    #             'age': 17,
    #             'hair_color': 'black',
    #             'married': False
    #         }
    #     }

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
        description="person name, needs a value greater than 0 and less than 50",
        example='manuel'
    ),
    age: Optional[int] = Query(
        ...,
        gt=0,
        it=1000,
        example=17
        )

):
    return {name: age}

#Validaciones: Path parameters
@app.get('/person/details/{person_id}')
def details(
    person_id: int = Path(
        ...,
        gt=0,
        title='person id',
        description='person id, the value must be greater than 0',
        example=1234567
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
        description='this is the person ID',
        example=1234567
        ),
    person: persona = Body(...),
    locate: located = Body(...)
    ):
    result = person.dict()
    result.update(locate.dict())
    return result
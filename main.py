from fastapi import FastAPI

app = FastAPI()
@app.get('/')
def home():
    return {'hello': 'world'}

@app.post('/person/new')
def new_person():
    pass
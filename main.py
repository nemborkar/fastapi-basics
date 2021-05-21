from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#db connection goes here
db = []

#models
class PokeBank(BaseModel):
    pk_name: str
    level: int
    nick: str


#index/landing
@app.get('/') 
def index():
    return {'key':'value'}
    

#gets all
@app.get('/pokemon')
def get_pokemon():
    return db


## might wanna call this caught
# @app.post('/pokemon')


## might wanna call this release
# @app.delete('/pokemon')




# @app.get('/pokemon/{poke_name}')



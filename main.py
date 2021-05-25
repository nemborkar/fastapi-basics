from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# db is a list, so can use statics values for now
db = [
    {
        "name": "Magikarp",
        "nick": "Kraken",
        "level": 18
    },
    {
        "name": "Gengar",
        "nick": "Shade",
        "level": 56
    },
    {
        "name": "Pidgeot",
        "nick": "aaabaaajss",
        "level": 88
    },
    {
        "name": "Bulbasaur",
        "nick": "Vines",
        "level": 5
    }
]

# models
class PokePC(BaseModel):
    name: str
    nick: str
    level: int
    


# index/landing
@app.get("/") 
async def index(token: str = Depends(oauth2_scheme)):
    return {"token_main": token}


# token endpoint; token gets created here by default
@app.post("/token") 
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {"access_token": form_data.username+"\'s token", "token_type": "bearer"}
    



# shows all pokemon in PC
@app.get("/pokemon")
async def show_pokemon():
    return db



# might wanna call this caught
@app.post("/pokemon")
async def store_pokemon(pokemon: PokePC): # pokemon here resembles something like the model PokePC
    db.append(pokemon.dict()) # converts pokemon to dictionary and then appends to the database (list?)
    return db[-1] # returns last one from the db



## might wanna call this release
@app.delete("/pokemon/{poke_id}")
async def release_pokemon(poke_id: int):
    db.pop(poke_id-1)
    return "Pokemon #"+str(poke_id)+" was released"



# @app.get('/pokemon/{poke_name}')



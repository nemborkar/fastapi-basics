from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="derp_token")

# db connection goes here?
# db is a list!
db = []

# models
class PokePC(BaseModel):
    name: str
    nick: str
    level: int
    


# index/landing
@app.get("/") 
def index(token: str = Depends(oauth2_scheme)):
    return {"token": token}
    

# shows all pokemon in PC
@app.get("/pokemon")
def show_pokemon():
    return db


# might wanna call this caught
@app.post("/pokemon")
def store_pokemon(pokemon: PokePC): # pokemon here resembles something like the model PokePC
    db.append(pokemon.dict()) # converts pokemon to dictionary and then appends to the database (list?)
    return db[-1] # returns last one from the db


## might wanna call this release
@app.delete("/pokemon/{poke_id}")
def release_pokemon(poke_id: int):
    db.pop(poke_id-1)
    return "Pokemon #"+str(poke_id)+" was released"



# @app.get('/pokemon/{poke_name}')



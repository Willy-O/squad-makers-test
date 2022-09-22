import json
from random import randint
from typing import Dict

import requests
from fastapi import APIRouter, Query, HTTPException
from pydantic import BaseModel, Field

from db.models.joke import Joke

router = APIRouter(
  prefix="/joke",
)

class NewJoke(BaseModel):
  text: str = Field(...)

def make_request(url: str, type_joke:str ='')-> dict:
  try:
    response = requests.get(url, headers={"Accept": "application/json"})
    data = response.json()
    return {
      "detail": "success",
      "results": data
      }
  except Exception as e:
    print(type(e))
    raise HTTPException(
      status_code=500,
      detail=f"Error getting the {type_joke} joke",
    )

@router.get("/")
async def get_random(type: str = Query(None)):
  chuck_url = 'https://api.chucknorris.io/jokes/random'
  dad_url = 'https://icanhazdadjoke.com/'
  if(type):
    typeL = type.lower()
    if(typeL != 'chuck' and typeL != 'dad'):
      raise HTTPException(
        status_code=400,
        detail="Just can pass 'chuck' or 'dad' as path params",
      )
    if(typeL == 'chuck'):
      return make_request(chuck_url, 'chuck')
    if(typeL == 'dad'):
      return make_request(dad_url, 'dad')
  else:
    request_url = chuck_url
    num = randint(0,1)
    if(num):
      request_url = dad_url
    return make_request(request_url)

@router.get("/myself")
async def get_myself():
  obj_joke = Joke()
  try:
    data = obj_joke.get_all()
    return {
      "detail": "success",
      "results": data
    }
  except Exception as e:
    print()
    raise HTTPException(
      status_code=400,
      detail="error getting myself jokes",
    )

@router.post("/")
async def post_myself(data: NewJoke):
  obj_joke = Joke()
  try:
    obj_joke.insert_one(data.parse_obj(data).dict())
    return {
      "detail": "success",
      "results": "save successful"
    }
  except Exception as e:
    print(type(e))
    print(e)
    raise HTTPException(
      status_code=400,
      detail="error insertting myself jokes",
    )

# POST: guardará en una base de datos el chiste (texto pasado por parámetro) ✅
# UPDATE: actualiza el chiste con el nuevo texto sustituyendo al chiste indicado en el parámetro “number” 
# DELETE: elimina el chiste indicado en el parametro number.

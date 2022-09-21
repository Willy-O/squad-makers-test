import json
from random import randint

import requests
from fastapi import APIRouter, Query, HTTPException

router = APIRouter(
  prefix="/joke",
)

def make_request(url: str, type_joke:str ='')-> dict:
  try:
    response = requests.get(url, headers={"Accept": "application/json"})
    data = response.json()
    return {
      "detail": "success",
      "result": data
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




# se envía el path param habrá que comprobar si tiene el valor “Chuck” o el valor “Dad” ✅
# devolverá un chiste aleatorio si no se pasa ningún path param. ✅
# si tiene el valor “Chuck” se conseguirá el chiste de este API ✅
# si tiene el valor “Dad” se conseguirá del API ✅
# en caso de que el valor no sea ninguno de esos dos se devolverá el error correspondiente. ✅

# POST: guardará en una base de datos el chiste (texto pasado por parámetro)
# UPDATE: actualiza el chiste con el nuevo texto sustituyendo al chiste indicado en el parámetro “number”
# DELETE: elimina el chiste indicado en el parametro number.


# fetch('https://icanhazdadjoke.com/',{
#     headers: {
#       'Content-Type': 'application/json'
#     },
# }).then(e=>e.json()).then(console.log).catch(console.error)
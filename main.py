from routes import joke, math
from fastapi import FastAPI
from db.conexion import Conexion

app = FastAPI()

app.include_router(joke.router)
app.include_router(math.router)

@app.get("/")
async def root():
  obj_conexion = Conexion()
  print(obj_conexion.create_database())
  return {"message": "Hi from my api"}

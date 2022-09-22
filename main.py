from routes import joke, math
from fastapi import FastAPI
# Discoment next line if you want to create the database
# from db.conexion import Conexion

app = FastAPI()

app.include_router(joke.router)
app.include_router(math.router)

@app.get("/")
async def root():
  # Discoment next lines if you want to create the database
  # obj_conexion = Conexion()
  # print(obj_conexion.create_database())
  return {"message": "Hi from my api"}

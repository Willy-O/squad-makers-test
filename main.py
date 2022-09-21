from routes import joke, math
from fastapi import FastAPI

app = FastAPI()

app.include_router(joke.router)
app.include_router(math.router)

@app.get("/")
async def root():
  return {"message": "Hi from my api"}


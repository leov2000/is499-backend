from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
import uvicorn
import random
import sqlite3
from config import PORT, RELOAD

app = FastAPI()

app.mount("/static", StaticFiles(directory="./static"), name="static")
templates = Jinja2Templates(directory="./template")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "cache_bust": random.random()})

if __name__ == "__main__":
    print("its running")
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=RELOAD, debug=RELOAD)


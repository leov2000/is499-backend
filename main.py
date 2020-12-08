from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import uvicorn
import random
from config import PORT, RELOAD
from db.query_tables import query_all, query_bully_table, query_consolidated, query_absences
from db.utils import connect_and_query, transform_to_dict
from db.config import headers

app = FastAPI()

app.mount("/static", StaticFiles(directory="./static"), name="static")
templates = Jinja2Templates(directory="./template")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "cache_bust": random.random()})

@app.get("/all")
async def all(request: Request):
    rows = connect_and_query("./db/schools.db", query_all())
    header_dict = headers["all"]
    result = jsonable_encoder(transform_to_dict(rows,header_dict))

    return JSONResponse(content=result)

@app.get("/bully")
async def bully(request: Request):
    rows = connect_and_query("./db/schools.db", query_bully_table())
    header_dict = headers["bully"]
    result = jsonable_encoder(transform_to_dict(rows,header_dict))

    return JSONResponse(content=result)

@app.get("/absent")
async def absent(request: Request):
    rows = connect_and_query("./db/schools.db", query_absences())
    header_dict = headers["absent"]
    result = jsonable_encoder(transform_to_dict(rows,header_dict))

    return JSONResponse(content=result)

@app.get("/consolidated")
async def consolidated(request: Request):
    rows = connect_and_query("./db/schools.db", query_consolidated())
    header_dict = headers["consolidated"]
    result = jsonable_encoder(transform_to_dict(rows,header_dict))

    return JSONResponse(content=result)

if __name__ == "__main__":
    print("its running")
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=RELOAD, debug=RELOAD)

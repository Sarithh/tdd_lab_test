from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Sarith"}

@app.get("/callname/{name}")
def read_name(name: str ):
    return {"hello":name}

@app.get("/callname")
def write_name(name: dict):
    name = data.get("name")
    return {"hello":name}


handler = Mangum(app)

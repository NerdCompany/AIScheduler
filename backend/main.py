from dotenv import dotenv_values
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

frontend = dotenv_values(".env")["FRONT_ENV"]
local = dotenv_values(".env")["LOCAL_ENV"]

app = FastAPI()
origins = [frontend, local]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/hi/")
def say_hi(name: str):
    return {"Hi": name}

from dotenv import dotenv_values
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origin = dotenv_values(".env")["FRONT_ENV"]

app = FastAPI()
origins = [origin]
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

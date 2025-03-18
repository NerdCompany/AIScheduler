from dotenv import dotenv_values
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import select, update
from db import engine, Scheduler

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


@app.get("/schedules")
def read_schedules(day: str):
    with Session(engine) as S:
        filter_by_day = select(Scheduler).where(Scheduler.day.in_([day]))
        out = S.execute(filter_by_day).all()
        output = [row[0] for row in out]
    
    return {
        "output": output
    }

@app.post("/add/")
def insert_event(day: str, time: int, name: str):
    with Session(engine) as S:
        first = Scheduler(day = day, time = time, name = name)

        S.add_all([first])
        S.commit()

    return {
        "message": "wena ctm"
    }

@app.put("/update/")
def update_by_day(day: str, new_name: str):
    with Session(engine) as S:
        day = update(Scheduler).where(Scheduler.day.in_([day])).values(name = new_name)

        result = S.execute(day)

        S.commit()

    return {
        "message": "apdeiteado"
    }
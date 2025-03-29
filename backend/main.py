from dotenv import dotenv_values
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from db import engine, Scheduler
from typing import Literal
from myTypes import Appointment, Weekdays, Time

frontend = dotenv_values(".env")["FRONT_ENV"]
local = dotenv_values(".env")["LOCAL_ENV"]

app = FastAPI()
origins: list = [frontend, local]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/schedules")
## TO DO: FIX THIS TYPE
def read_schedules(
    day: Literal[
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ],
):
    with Session(engine) as s:
        filter_by_day = select(Scheduler).where(Scheduler.day.in_([day]))
        out = s.execute(filter_by_day).all()
        output = [row[0] for row in out]

    return {"output": output}


@app.post("/add/")
def insert_event(event: Appointment):
    with Session(engine) as s:
        first = Scheduler(day=event.day.name, time=event.time.hour, name=event.name)

        s.add_all([first])
        s.commit()

    return {"message": "wena ctm"}


@app.put("/update/")
def update_by_day(day: Weekdays, time: Time, new_name: str):
    with Session(engine) as s:
        day = (
            update(Scheduler)
            .where(Scheduler.day.in_([day.name]))
            .where(Scheduler.time.in_([time.hour]))
            .values(name=new_name)
        )

        result = s.execute(day)

        s.commit()

    return {"message": "apdeiteado"}


@app.delete("/delete/")
def delete_by_time(day: Weekdays, time: Time):
    with Session(engine) as s:
        date_time = (
            delete(Scheduler)
            .where(Scheduler.time == time.hour)
            .where(Scheduler.day == day.name)
        )

        result = s.execute(date_time)

        s.commit()

    return {"message": "deleteado"}

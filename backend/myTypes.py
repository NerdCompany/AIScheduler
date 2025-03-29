from typing import Literal
from pydantic import BaseModel, Field

class Weekdays(BaseModel):
    name: Literal[
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]

class Time(BaseModel):
    hour: int = Field(gt=0, le=24)

class Appointment(BaseModel):
    day: Weekdays
    time: Time
    name: str

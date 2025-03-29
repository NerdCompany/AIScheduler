from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import String, create_engine


class Base(DeclarativeBase):
    pass


class Scheduler(Base):
    __tablename__ = "scheduler"
    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[str] = mapped_column(String(10))
    time: Mapped[int]
    name: Mapped[str] = mapped_column(String(20))


engine = create_engine("sqlite:///scheduler.db")

if __name__ == "__main__":
    Base.metadata.create_all(engine)

    print("db succesfully created!!")

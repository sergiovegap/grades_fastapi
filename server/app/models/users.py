from datetime import date
from sqlalchemy import Column, String, Enum, DateTime, Boolean, Date, JSON
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from .base import Base

# User types
class Role():
    ADMINISTRATIVE = "Administrative"
    PROFESSOR = "Professor"
    STUDENT = "Student"


# Teacher
class Professor(Base):
    __tablename__ = "professor"

    id: Mapped[str] = mapped_column(String(100), primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    lastName: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    profile: Mapped[str] = mapped_column(String(100), nullable=False)
    subjects:  Mapped[str] = mapped_column(String(100), nullable=False)

    def get_full_name(self):
        return f"'name': {self.name}, 'lastName': {self.lastName}"


# Student
class Student(Base):
    __tablename__ = "student"

    id: Mapped[str] = mapped_column(String(100), primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    lastName: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    profile: Mapped[str] = mapped_column(String(100), nullable=False)
    # status: Mapped[bool] = mapped_column(Boolean, default=True)
    enrollment: Mapped[date] = mapped_column(Date, default=date.today, onupdate=date.today)
    subjects:  Mapped[str] = mapped_column(String(100), nullable=False)

    def get_full_name(self):
        return {"name": self.name, "lastName": self.lastName}

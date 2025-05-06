from pydantic import BaseModel, Field, EmailStr, Dict
from enum import StrEnum
from datetime import datetime
from uuid import uuid4


# User types
class Role(StrEnum):
    ADMINISTRATIVE = "Administrative"
    PROFESSOR = "Professor"
    STUDENT = "Student"

# Teacher
class Professor(BaseModel):
    id: str = Field(min_length=5, max_length=100, default_factory=uuid4)
    name: str = Field(min_length=5, max_length=100)
    lastName: str = Field(min_length=5, max_length=100)
    email: str = Field(min_length=5, max_length=100)
    profile: str = Field(min_length=5, max_length=100)
    # subjects: str = Field(min_length=5, max_length=100)


# Student
class Student(BaseModel):
    id: str = Field(min_length=5, max_length=100, default_factory=uuid4)
    name: str = Field(min_length=5, max_length=100)
    lastName: str = Field(min_length=5, max_length=100)
    email: str = Field(min_length=5, max_length=100)
    profile: str = Field(min_length=5, max_length=100)
    # status: bool = Field(True)
    # enrollment = datetime=datetime.now()
    subjects: str = Field(min_length=5, max_length=100)
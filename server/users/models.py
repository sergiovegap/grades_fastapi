from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Grades
class Grade():
    first_grade: float
    second_grade: float
    third_grade: float
    final_grade: float

# Subjects
class Subject():
    id: Optional[int] = None
    subject: str
    description: str
    professor: str


# General user
class User(BaseModel):
    id: Optional[int] = None
    name: str
    lastName: str
    role: str
    profile: str
    subjects: dict = dict[int: str]
    enrollment: datetime=datetime.now()


# Teacher
class Professor(User):
    pass


# Student
class Student(BaseModel):
    pass
from pydantic import Field
from uuid import uuid4

# Grades
class Grade():
    id: str = Field(default_factory=uuid4)
    id_alumno: str = Field(min_length=5, max_length=200)
    id_subject: str = Field(min_length=5, max_length=200)
    grade: float = Field(min_length=5, max_length=3)


# Subjects
class Subject():
    id: str = Field(default_factory=uuid4)
    title: str = Field(min_length=5, max_length=200)
    description: str = Field(min_length=5, max_length=500)
    professor: str = Field(min_length=5, max_length=200)
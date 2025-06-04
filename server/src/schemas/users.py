from pydantic import BaseModel, EmailStr, Field
from enum import StrEnum
from datetime import date, datetime
from typing import List, Optional
from src.schemas.subjects import SubjectScheme, GradeScheme


# User types
class Role(StrEnum):
    SECRETARY = "Secretary"
    PRINCIPAL = "Principal"
    LIBRARIAN = "Librarian"
    COUNSELOR = "Counselor"
    ADMINISTRATIVE = "Administrative"

# ADMINISTRATIVES
# User register
class AdminRegisterScheme(BaseModel):
    name: str = Field(max_length=100)
    lastname: str = Field(max_length=100)
    email: str = Field(max_length=100)
    role: str = Field(max_length=100)

    class Config:
        from_attributes = True

# Update user
class AdminSchemeUpdate(BaseModel):
    name: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    profile: Optional[str] = None
    role: Optional[str] = None

    class Config:
        from_attributes = True

# Out user
class AdminScheme(BaseModel):
    id: str = Field(max_length=100)
    name: str = Field(max_length=100)
    lastname: str = Field(max_length=100)
    email: str = Field(max_length=100)
    profile: Optional[str] = Field(max_length=1000)
    password: str = Field(min_length=5, max_length=100)
    role: Role
    created_at: datetime

    class Config:
        from_attributes = True

# Create professor
class ProfessorRegisterScheme(BaseModel):
    name: str = Field(max_length=100)
    lastname: str = Field(max_length=100)
    email: str = Field(min_length=5, max_length=100)

    class Config:
        from_attributes = True

# Update professor
class ProfessorSchemeUpdate(BaseModel):
    name: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    profile: Optional[str] = None

    class Config:
        from_attributes = True

# Output
class ProfessorScheme(BaseModel):
    id: str = Field(max_length=100)
    name: str = Field(max_length=100)
    lastname: str = Field(max_length=100)
    email: str = Field(min_length=5, max_length=100)
    profile: Optional[str] = Field(max_length=1000)
    password: str = Field(min_length=5, max_length=100)
    subjects: List[SubjectScheme] = []
    created_at: datetime

    class Config:
        from_attributes = True

# Create student
class StudentRegisterScheme(BaseModel):
    name: str = Field(max_length=100)
    lastname: str = Field(max_length=100)
    email: str = Field(max_length=100)

    class Config:
        from_attributes = True

# Update student
class StudentSchemeUpdate(BaseModel):
    name: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    profile: Optional[str] = None
    subjects: Optional[List[SubjectScheme]] = None
    grades: Optional[List[GradeScheme]] = None

    class Config:
        from_attributes = True

# Output
class StudentScheme(BaseModel):
    # Fields
    id: str = Field(max_length=100)
    name: str = Field(max_length=100)
    lastname: str = Field(max_length=100)
    email: str = Field(max_length=100)
    profile: Optional[str] = Field(max_length=1000)
    password: str = Field(min_length=5, max_length=100)
    status: bool = Field(True)
    enrollment: date = None

    # Relations
    subjects: List[SubjectScheme] = []
    grades: List[GradeScheme] = []

    class Config:
        from_attributes = True
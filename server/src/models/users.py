from datetime import date
from typing import Optional
from nanoid import generate
from sqlalchemy import Column, ForeignKey, String, Boolean, Date, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database.database import Base

student_subjects = Table(
    "student_subjects",
    Base.metadata,
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("subject_id", ForeignKey("subjects.id"), primary_key=True)
)

# Administrative
class Administrative(Base):
    __tablename__ = "administratives"

    id: Mapped[str] = mapped_column(String(100), primary_key=True, default=lambda: generate(size=8))
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    lastname: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    password: Mapped[str] = mapped_column(String(100), default=generate(size=8), nullable=False)
    profile: Mapped[Optional[str]] = mapped_column(String(1000), nullable=True)
    role: Mapped[str] = mapped_column(String(1000), nullable=True)
    created_at: Mapped[date] = mapped_column(Date, default=date.today, onupdate=date.today)

    def get_full_name(self):
        return f"'name': {self.name}, 'lastname': {self.lastname}"
    

# Professor
class Professor(Base):
    __tablename__ = "professors"

    # Fields
    id: Mapped[str] = mapped_column(String(100), primary_key=True, default=lambda: generate(size=8))
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    lastname: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), default=generate(size=8), nullable=False)
    profile: Mapped[Optional[str]] = mapped_column(String(1000), nullable=True)
    created_at: Mapped[date] = mapped_column(Date, default=date.today, onupdate=date.today)

    # Relations
    subjects = relationship("Subject", back_populates="professor")

    def get_full_name(self):
        return f"'name': {self.name}, 'lastname': {self.lastname}"


# Student
class Student(Base):
    __tablename__ = "students"

    # Fields
    id: Mapped[str] = mapped_column(String(100), primary_key=True, default=lambda: generate(size=8))
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    lastname: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), default=generate(size=8), nullable=False)
    profile: Mapped[Optional[str]] = mapped_column(String(1000), nullable=True)
    status: Mapped[bool] = mapped_column(Boolean, default=True)
    enrollment: Mapped[date] = mapped_column(Date, default=date.today, onupdate=date.today)

    # Relations
    subjects = relationship("Subject", secondary=student_subjects, back_populates="students")
    grades = relationship("Grade", back_populates="student")

    def get_full_name(self):
        return {"name": self.name, "lastname": self.lastname}




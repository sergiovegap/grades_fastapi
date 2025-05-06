from enum import StrEnum
from sqlalchemy import Column, String, Enum, DateTime, Boolean, Double, Integer
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

# Grades
class Grade(Base):
    __tablename__ = "grade"

    id = Column(String, primary_key=True, autoincrement=False)
    id_alumno = mapped_column(ForeignKey("student.id"))
    id_subject = mapped_column(ForeignKey("subject.id"))
    grade: Mapped[int] = mapped_column(Integer, nullable=False)
    # subject = relationship("subject", backref="subject")


# Subjects
class Subject(Base):
    __tablename__ = "subject"

    id = Column(String, primary_key=True, autoincrement=False)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=False)
    professor = mapped_column(ForeignKey("professor.id", ondelete="CASCADE"))
    subject = relationship("professor", backref="professor")
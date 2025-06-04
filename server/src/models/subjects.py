from nanoid import generate
from sqlalchemy import String, Float, UniqueConstraint
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.database.database import Base
from src.models.users import student_subjects

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# Grades
class Grade(Base):
    __tablename__ = "grades"

    # Fields
    id: Mapped[str] = mapped_column(String(100), primary_key=True, default=lambda: generate(alphabet=alphabet, size=8))
    id_student: Mapped[str] = mapped_column(ForeignKey("students.id"), nullable=False)
    id_subject: Mapped[str] = mapped_column(ForeignKey("subjects.id"), nullable=False)
    grade: Mapped[float] = mapped_column(Float, nullable=False)

    # Restrictions
    __table_args__ = (
        UniqueConstraint('id_student', 'id_subject', name='uq_student_subject'),
    )

    # Relations
    subject = relationship("Subject", back_populates="grades")
    student = relationship("Student", back_populates="grades")


# Subjects
class Subject(Base):
    __tablename__ = "subjects"

    # Fields
    id: Mapped[str] = mapped_column(String(100), primary_key=True, default=lambda: generate(alphabet=alphabet, size=8))
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=False)
    professor_id: Mapped[str] = mapped_column(ForeignKey("professors.id"), nullable=False)

    # Relations
    students = relationship("Student", secondary=student_subjects, back_populates="subjects")
    professor = relationship("Professor", back_populates="subjects")
    grades = relationship("Grade", back_populates="subject")

    def get_title(self):
        return {"title": self.title, "description": self.description}

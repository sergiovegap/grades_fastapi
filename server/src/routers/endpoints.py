from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from src.database.database import session, get_db
from src.schemas.users import *
from src.schemas.subjects import *
from src.models.users import Professor, Student, Administrative
from src.models.subjects import Grade, Subject

users_router = APIRouter()
subjects_router = APIRouter()

# Register administrative
@users_router.post("/create-administrative/", response_model=AdminScheme)
def create_administrative(user: AdminRegisterScheme, db: session = Depends(get_db)):  # type: ignore
    db_user = Administrative(
        name=user.name, lastname=user.lastname, email=user.email, role=user.role)

    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "Administrative registered successfuly.",
                "subject": {
                    "id": db_user.id,
                    "name": db_user.name,
                    "lastname": db_user.lastname,
                    "email": db_user.email
                }
            }
        )

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Administrative cannot be registered."
        )


# Register student
@users_router.post("/create-student/", response_model=StudentScheme)
def create_student(user: StudentRegisterScheme, db: session = Depends(get_db)):  # type: ignore
    db_user = Student(name=user.name, lastname=user.lastname, email=user.email)

    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "Student registered successfuly.",
                "subject": {
                    "id": db_user.id,
                    "name": db_user.name,
                    "lastname": db_user.lastname,
                    "email": db_user.email
                }
            }
        )

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Student cannot be registered."
        )


# Register professor
@users_router.post("/create-professor/", response_model=ProfessorScheme)
def create_professor(user: ProfessorRegisterScheme, db: session = Depends(get_db)):  # type: ignore
    db_user = Professor(
        name=user.name, lastname=user.lastname, email=user.email)

    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "Professor registered successfully.",
                "subject": {
                    "id": db_user.id,
                    "name": db_user.name,
                    "lastname": db_user.lastname,
                    "email": db_user.email
                }
            }
        )

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Professor cannot be registered."
        )


# Create subject
@subjects_router.post("/create-subject/", response_model=SubjectScheme)
def create_subject(subject: SubjectRegisterScheme, db: session = Depends(get_db)):  # type: ignore
    db_subject = Subject(
        title=subject.title, description=subject.description, professor_id=subject.professor_id)

    try:
        db.add(db_subject)
        db.commit()
        db.refresh(db_subject)

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "Materia creada exitosamente.",
                "subject": {
                    "id": db_subject.id,
                    "title": db_subject.title,
                    "description": db_subject.description,
                    "professor_id": db_subject.professor_id
                }
            }
        )

    except IntegrityError as e:
        db.rollback()
        # Puede ser una clave foránea inválida o algo similar
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se pudo crear la materia. Verifica que el ID del profesor exista."
        )

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ocurrió un error inesperado al crear la materia."
        )


# Get administratives
@users_router.get("/administratives/", response_model=List[AdminScheme])
def get_administratives(db: session = Depends(get_db)):  # type: ignore
    administratives = db.query(Administrative).all()

    return administratives


# Get students
@users_router.get("/students/", response_model=List[StudentScheme])
def get_students(db: session = Depends(get_db)):  # type: ignore
    students = db.query(Student).all()

    return students


# Get professors
@users_router.get("/professors/", response_model=List[ProfessorScheme])
def get_professors(db: session = Depends(get_db)):  # type: ignore
    professors = db.query(Professor).all()

    return professors


# Get administrative by id
@users_router.get("/administrative/${id}", response_model=AdminScheme)
def get_administrative_by_id(id: str, db: session = Depends(get_db)):  # type: ignore
    administrative = db.query(Administrative).filter(
        Administrative.id == id).first()

    if not administrative:
        raise HTTPException(
            status_code=404, detail="!Administrative not found!")

    return administrative


# Get student by id
@users_router.get("/student/${id}", response_model=StudentScheme)
def get_student_by_id(id: str, db: session = Depends(get_db)):  # type: ignore
    student = db.query(Student).filter(Student.id == id).first()

    if not student:
        raise HTTPException(status_code=404, detail="!Student not found!")

    return student


# Get professor by id
@users_router.get("/professor/${id}", response_model=ProfessorScheme)
def get_professor_by_id(id: str, db: session = Depends(get_db)):  # type: ignore
    professor = db.query(Professor).filter(Professor.id == id).first()

    if not professor:
        raise HTTPException(status_code=404, detail="!Professor not found!")

    return professor


# Update Administrative
@users_router.patch("/update-administrative/${id}", response_model=AdminSchemeUpdate)
def update_administrative(id: str, update_data: AdminSchemeUpdate, db: session = Depends(get_db)):  # type: ignore
    administrative = db.query(Administrative).filter(
        Administrative.id == id).first()

    if not administrative:
        raise HTTPException(
            status_code=404, detail="!Administrative not found!")

    update_data_dict = update_data.model_dump(exclude_unset=True)

    for field, value in update_data_dict.items():
        setattr(administrative, field, value)

    db.commit()
    db.refresh(administrative)

    return administrative


# Update student
@users_router.patch("/update-student/${id}", response_model=StudentScheme)
def update_student(id: str, update_data: StudentSchemeUpdate, db: session = Depends(get_db)):  # type: ignore
    student = db.query(Student).filter(Student.id == id).first()

    if not student:
        raise HTTPException(status_code=404, detail="!Student not found!")

    # Solo actualiza los campos que están presentes
    for field, value in update_data.model_dump(exclude_unset=True).items():
        setattr(student, field, value)

    db.commit()
    db.refresh(student)

    return student


# Update student
@users_router.patch("/update-professor/${id}", response_model=ProfessorSchemeUpdate)
def update_professor(id: str, update_data: ProfessorSchemeUpdate, db: session = Depends(get_db)):  # type: ignore
    professor = db.query(Professor).filter(Professor.id == id).first()

    if not professor:
        raise HTTPException(status_code=404, detail="!Professor not found!")

    # Solo actualiza los campos que están presentes
    for field, value in update_data.model_dump(exclude_unset=True).items():
        setattr(professor, field, value)

    db.commit()
    db.refresh(professor)

    return professor


# Delete administrative
@users_router.delete("/delete-administrative/${id}", status_code=200)
def delete_administrative(id: str, db: session = Depends(get_db)):  # type: ignore
    administrative = db.query(Administrative).filter(
        Administrative.id == id).first()

    if not administrative:
        raise HTTPException(status_code=404, detail="!Professor not found!")

    db.delete(administrative)
    db.commit()

    return {"message": "Usuario administrativo eliminado correctamente"}


# Delete student
@users_router.delete("/delete-student/${id}", status_code=200)
def delete_student(id: str, db: session = Depends(get_db)):  # type: ignore
    student = db.query(Student).filter(Student.id == id).first()

    if not student:
        raise HTTPException(status_code=404, detail="!Professor not found!")

    db.delete(student)
    db.commit()

    return {"message": "Usuario administrativo eliminado correctamente"}


# Delete professor
@users_router.delete("/delete-professor/${id}", status_code=200)
def delete_professor(id: str, db: session = Depends(get_db)):  # type: ignore
    professor = db.query(Professor).filter(Professor.id == id).first()

    if not professor:
        raise HTTPException(status_code=404, detail="!Professor not found!")

    db.delete(professor)
    db.commit()

    return {"message": "Usuario administrativo eliminado correctamente"}


# Asign subject
@users_router.post("/asign-subject/${id}", response_model=StudentScheme)
def asign_subject(id: str, update_data: AsignSubjectScheme, db: session = Depends(get_db)):  # type: ignore
    student = db.query(Student).filter(Student.id == id).first()

    if not student:
        raise HTTPException(status_code=404, detail="!Student not found!")

    subjects_to_add = db.query(Subject).filter(Subject.id.in_(update_data.subjects)).all()

    if not subjects_to_add:
        raise HTTPException(
            status_code=404, detail="!Subject not found!")

    for subject in subjects_to_add:
        if subject not in student.subjects:
            student.subjects.append(subject)

    db.commit()
    db.refresh(student)

    return student


# Asign grade
@users_router.post("/asign-grade/${id}", response_model=GradeScheme)
def asign_grade(id: str, grade: AsignGradeScheme, db: session = Depends(get_db)):  # type: ignore
    student = db.query(Student).filter(Student.id == id).first()

    if not student:
        raise HTTPException(status_code=404, detail="!Student not found!")
    
    subjects_to_add = db.query(Subject).filter(Subject.id == grade.id_subject).first()

    if not subjects_to_add:
        raise HTTPException(status_code=404, detail="!Subject not found!")

    db_grade = Grade(id_student=id, id_subject=grade.id_subject, grade=grade.grade)

    try:
        db.add(db_grade)
        db.commit()
        db.refresh(db_grade)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Grade already exists for this student and subject.")

    return db_grade


# Modify grade
@users_router.patch("/update-grade/${id}", response_model=GradeScheme)
def update_grade(id: str, grade: UpgradeGradeScheme, db: session = Depends(get_db)):  # type: ignore
    student = db.query(Student).filter(Student.id == id).first()
    subject = db.query(Subject).filter(Subject.id == grade.id_subject).first()
    existing_grade = db.query(Grade).filter(Grade.id_student == id, Grade.id_subject == grade.id_subject).first()

    if not student:
        raise HTTPException(status_code=404, detail="!Student not found!")

    if not subject:
        raise HTTPException(status_code=404, detail="!Subject not found!")

    if existing_grade:
        # Upgrade existing grade
        existing_grade.grade = grade.grade
        db.commit()
        db.refresh(existing_grade)
        return existing_grade
    else:
        # Asign new grade
        new_grade = Grade(id_student=id, id_subject=grade.id_subject, grade=grade.grade)
        db.add(new_grade)
        db.commit()
        db.refresh(new_grade)
        return new_grade

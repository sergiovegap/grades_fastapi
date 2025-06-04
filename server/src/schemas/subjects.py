from typing import List, Optional
from pydantic import BaseModel, Field

# Update grade
class UpgradeGradeScheme(BaseModel):
    id_subject: Optional[str] = None
    grade: Optional[float] = None

# Asign grade
class AsignGradeScheme(BaseModel):
    id_subject: str = Field(min_length=5, max_length=200)
    grade: float = Field(ge=0.0, le=10.0)

# Grades
class GradeScheme(BaseModel):
    id: str = Field(max_length=100)
    id_student: str = Field(min_length=5, max_length=200)
    id_subject: str = Field(min_length=5, max_length=200)
    grade: float = Field(ge=0.0, le=10.0)

    class Config:
        from_attributes = True

# Asign subject scheme
class AsignSubjectScheme(BaseModel):
    subjects: List[str]

    class Config:
        from_attributes = True

# Subject register scheme
class SubjectRegisterScheme(BaseModel):
    title: str = Field(max_length=200)
    description: str = Field(max_length=2000)
    professor_id: str = Field(max_length=50)

    class Config:
        from_attributes = True

# Subject update scheme
class SubjectUpdateScheme(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    professor_id: Optional[str] = None

    class Config:
        from_attributes = True

# Subject create
class SubjectScheme(BaseModel):
    id: str = Field(max_length=100)
    title: str = Field(max_length=200)
    description: str = Field(max_length=2000)
    professor_id: str = Field(max_length=50)

    class Config:
        from_attributes = True

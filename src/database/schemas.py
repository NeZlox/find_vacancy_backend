from typing import Optional

from pydantic import BaseModel, ConfigDict


class Url_Schema(BaseModel):
    id: int
    url: str

    model_config = ConfigDict(from_attributes=True)

class Url_CreateSchema(BaseModel):
    url: str

    model_config = ConfigDict(from_attributes=True)

class Url_UpdateSchema(BaseModel):
    id: Optional[int] = None
    name: str

    model_config = ConfigDict(from_attributes=True)





class Vacancy_Schema(BaseModel):
    id: int
    title: Optional[str] = None
    salary: Optional[str] = None
    experience: Optional[str] = None
    work_format: Optional[str] = None
    description: Optional[str] = None
    vacancy_vector: Optional[str] = None


    id_url: int

    model_config = ConfigDict(from_attributes=True)

class Vacancy_CreateSchema(BaseModel):
    title: Optional[str] = None
    salary: Optional[str] = None
    experience: Optional[str] = None
    work_format: Optional[str] = None
    description: Optional[str] = None
    vacancy_vector: Optional[str] = None


    id_url: int


    model_config = ConfigDict(from_attributes=True)

class Vacancy_UpdateSchema(BaseModel):
    id: int
    title: Optional[str] = None
    salary: Optional[str] = None
    experience: Optional[str] = None
    work_format: Optional[str] = None
    description: Optional[str] = None
    vacancy_vector: Optional[str] = None


    model_config = ConfigDict(from_attributes=True)



class Skills_Schema(BaseModel):
    id: int
    skill: str

    model_config = ConfigDict(from_attributes=True)

class Skills_CreateSchema(BaseModel):
    skill: str

    model_config = ConfigDict(from_attributes=True)

class Skills_UpdateSchema(BaseModel):
    id: Optional[int] = None
    skill: str

    model_config = ConfigDict(from_attributes=True)





class Skills_to_vacancy_Schema(BaseModel):
    id: int
    id_skills: int
    id_vacancies: int

    model_config = ConfigDict(from_attributes=True)

class Skills_to_vacancy_CreateSchema(BaseModel):
    id_skills: int
    id_vacancies: int

    model_config = ConfigDict(from_attributes=True)

class Skills_to_vacancy_UpdateSchema(BaseModel):
    id: int
    id_skills: Optional[int]
    id_vacancies: Optional[int]

    model_config = ConfigDict(from_attributes=True)

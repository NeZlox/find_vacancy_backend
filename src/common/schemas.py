from typing import Any, List, Literal, Optional

from pydantic import BaseModel, Field, model_validator

from src.database.schemas import Vacancy_Schema


class Response_Schemas(BaseModel):
    data: Any


class None_ListResponse(Response_Schemas):
    data: None


class findVacancy_QueryParamsSchemas(BaseModel):
    search_line: str

class Vacancy_DTO(Vacancy_Schema):
    url: str
    skills: Optional[List[str]] = None



class temp(BaseModel):
    id: int
    title: Optional[str] = None
    salary: Optional[str] = None
    experience: Optional[str] = None
    work_format: Optional[str] = None
    description: Optional[str] = None
    #vacancy_vector: Optional[str] = None

    #id_url: int

    url: str
    skills: Optional[List[str]] = None
class Vacancy_ListResponse(Response_Schemas):

    data: List[temp]


class Parsing_QueryParams(BaseModel):
    country: str = Field(default='volgograd', description="Country name")
    name: str = Field(default='programmist', description="Vacancy name")
    page_start: int = Field(default=0, description="Start page", ge=0)
    page_end: int = Field(default=0, description="End page", ge=0)

    @model_validator(mode='after')
    def validate_page(cls, value):
        if value.page_start > value.page_end:
            raise ValueError("page_start must be less than page_end")
        return value




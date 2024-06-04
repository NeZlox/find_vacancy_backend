from typing import Any, List, Literal, Optional

from pydantic import BaseModel, Field, model_validator
from fastapi import HTTPException, status
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
    # vacancy_vector: Optional[str] = None

    # id_url: int

    url: str
    skills: Optional[List[str]] = None


class Vacancy_ListResponse(Response_Schemas):
    data: List[temp]


class Parsing_QueryParams(BaseModel):
    country: str = Field(description="Country name") # ,default='volgograd')
    name: str = Field(description="Vacancy name")#    ,default='programmist')
    page_start: int = Field(description="Start page", ge=0) #   ,default=0,)
    page_end: int = Field(description="End page", ge=0) #   ,default=0,)

    @model_validator(mode='after')
    def validate_page(cls, value):
        if value.page_start > value.page_end:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Page start must be less than or equal to the page end")
        return value

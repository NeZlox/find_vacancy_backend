from fastapi import APIRouter, Depends, HTTPException

from src.common.schemas import (None_ListResponse, Parsing_QueryParams,
                                Vacancy_ListResponse,
                                findVacancy_QueryParamsSchemas)
from src.common.service import Common_Service
from src.exceptions import RequestHandlingError

__all__ = ['router']

router = APIRouter(tags=["Common"])


@router.get("/vacancy/", response_model=Vacancy_ListResponse)
async def get_vacancy(query_params: findVacancy_QueryParamsSchemas = Depends()):
    try:
        data = await Common_Service.get_vacancy_data(query_params.search_line)

        result = {
            "data": data
        }

        return result


    except (HTTPException, Exception) as e:

        raise RequestHandlingError


@router.get("/start_parsing/", response_model=None_ListResponse)
async def start_parsing(query_params: Parsing_QueryParams = Depends()):
    try:

        await Common_Service.start_parsing(**query_params.model_dump(mode='python'))

        result = {
            "data": None
        }

        return result


    except (HTTPException, Exception) as e:

        raise RequestHandlingError

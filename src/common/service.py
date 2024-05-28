from src.common.schemas import Vacancy_DTO
from src.common.utils import nikon
from src.database.queries import Vacancy_Query
from src.tasks import parse_hh


class Common_Service:

    @staticmethod
    async def get_vacancy_data(search_line: str):
        result_vacancies = await Vacancy_Query.select_all()

        result_vacancies_DTO = []
        for vacancy in result_vacancies:
            vacancy_dict = {
                "id": vacancy.id,
                "title": vacancy.title,
                "salary": vacancy.salary,
                "experience": vacancy.experience,
                "work_format": vacancy.work_format,
                "description": vacancy.description,
                "vacancy_vector": vacancy.vacancy_vector,
                "id_url": vacancy.id_url,
                "url": vacancy.url.url,
                "skills": [skill.skill for skill in vacancy.skills]
            }
            result_vacancies_DTO.append(Vacancy_DTO(**vacancy_dict))

        remaining = result_vacancies_DTO #await nikon(result_vacancies_DTO)
        return remaining

    @staticmethod
    async def start_parsing(country: str, name: str, page_start: int, page_end: int):
        parse_hh.delay(country, name, page_start, page_end)
        return None


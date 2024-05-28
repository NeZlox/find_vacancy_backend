from typing import Any, Dict

from sqlalchemy import create_engine, delete
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from src.config import settings
from src.database.models import *
from src.logger import logger
from src.tasks.celery_app import celery

sync_engine = create_engine(settings.DATABASE_URL_SYNC,pool_size=5, max_overflow=10 )#echo=True)
SyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=sync_engine,
    expire_on_commit=False
)

def nikon():
    pass

def insert_db(info_vacancy: Dict[str, Any]):

    url = info_vacancy['url']
    title = info_vacancy.get('title')
    salary = info_vacancy.get('salary')
    experience = info_vacancy.get('experience')
    work_format = info_vacancy.get('work_format')
    description = info_vacancy.get('description')
    vacancy_vector = nikon()
    skills = info_vacancy.get('skills')

    with SyncSessionLocal() as Session:
        try:
            # Проверяем существует ли запись с таким URL
            existing_url = Session.query(urlsModel).filter_by(url=url).first()

            if not existing_url:
                # Создаем новую запись URL
                new_url = urlsModel(url=url)
                Session.add(new_url)
                Session.commit()  # Делаем commit, чтобы получить ID новой записи
            else:
                new_url = existing_url

            # Проверяем существует ли запись о вакансии для данного URL
            existing_vacancy = Session.query(vacanciesModel).filter_by(id_url=new_url.id).first()

            if existing_vacancy:
                # Обновляем существующую запись о вакансии
                existing_vacancy.title = title
                existing_vacancy.salary = salary
                existing_vacancy.experience = experience
                existing_vacancy.work_format = work_format
                existing_vacancy.description = description
                existing_vacancy.vacancy_vector = vacancy_vector

                vacancy_id = existing_vacancy.id

            else:
                # Создаем новую запись о вакансии
                new_vacancy = vacanciesModel(
                    title=title,
                    salary=salary,
                    experience=experience,
                    work_format=work_format,
                    description=description,
                    vacancy_vector=vacancy_vector,
                    id_url=new_url.id
                )
                Session.add(new_vacancy)
                Session.commit()  # Делаем commit, чтобы получить ID новой записи о вакансии
                vacancy_id = new_vacancy.id

            # Добавляем или обновляем связи с навыками
            new_id_skill = set()
            if skills:
                for skill in skills:
                    # Проверяем существует ли навык в базе данных
                    existing_skill = Session.query(skillsModel).filter_by(skill=skill).first()
                    if not existing_skill:
                        # Создаем новый навык, если не найден
                        new_skill = skillsModel(skill=skill)
                        Session.add(new_skill)
                        Session.commit()  # Делаем commit, чтобы получить ID нового навыка
                    else:
                        new_skill = existing_skill

                    new_id_skill.add(new_skill.id)
                    # Проверяем существует ли связь между вакансией и навыком
                    existing_relation = Session.query(skills_to_vacancyModel).filter_by(id_skill=new_skill.id, id_vacancy=vacancy_id).first()
                    if not existing_relation:
                        # Создаем новую связь между вакансией и навыком
                        new_relation = skills_to_vacancyModel(id_skill=new_skill.id, id_vacancy=vacancy_id)
                        Session.add(new_relation)


            existing_id_skill = Session.query(skills_to_vacancyModel.id_skill).filter_by(id_vacancy=vacancy_id).all()
            existing_id_skill = {record.id_skill for record in existing_id_skill}

            records_to_delete = existing_id_skill - new_id_skill
            if records_to_delete:
                stmt = (
                    delete(skills_to_vacancyModel)
                    .where(skills_to_vacancyModel.id_vacancy == vacancy_id)
                    .where(skills_to_vacancyModel.id_skill.in_(records_to_delete))
                )
                Session.execute(stmt)
            Session.commit()
        except (SQLAlchemyError, Exception) as e:
            Session.rollback()
            logger.info(f"Функция insert_db\n{e}\n\n")







@celery.task
def insert_db_task(info_vacancy: Dict[str, Any]):
    #logger.info(f"Функция insert_db_task {info_vacancy}")
    insert_db(info_vacancy)
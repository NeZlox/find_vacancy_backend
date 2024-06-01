import datetime
from typing import Annotated, Optional

from sqlalchemy import ForeignKey, String, Text, UniqueConstraint, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]
template_created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
template_updated_at = Annotated[datetime.datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"),
    onupdate=datetime.datetime.now(datetime.UTC)
)]

class urlsModel(Base):
    __tablename__ = "urls"

    id: Mapped[intpk]
    url: Mapped[str] = mapped_column(Text)

    created_at: Mapped[template_created_at]
    updated_at: Mapped[template_updated_at]

    __table_args__ = (
        UniqueConstraint('url', name='urls_unique_url'),
    )

    vacancy: Mapped["vacanciesModel"] = relationship( # создание переменной и указание подгружаемой модели к текущей модели
        back_populates="url",  # Здесь изменено на "url" ссылка на переменую в другой таблице
        uselist=False,
        cascade="all, delete"
    )

class vacanciesModel(Base):
    __tablename__ = "vacancies"

    id: Mapped[intpk]
    title: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    salary: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    experience: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    work_format: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    vacancy_vector: Mapped[Optional[str]] = mapped_column(Text, nullable=True, server_default=None)

    id_url: Mapped[int] = mapped_column(ForeignKey("urls.id", ondelete="CASCADE", onupdate="CASCADE"))

    created_at: Mapped[template_created_at]
    updated_at: Mapped[template_updated_at]


    __table_args__ = (
        UniqueConstraint('id_url', name='vacancies_unique_id_url'),
    )

    url: Mapped["urlsModel"] = relationship(
        back_populates="vacancy"  # Здесь изменено на "vacancy"
    )

    skills: Mapped[list["skillsModel"]] = relationship(
        secondary="skills_to_vacancy",
        back_populates="vacancies"
    )

class skillsModel(Base):
    __tablename__ = "skills"

    id: Mapped[intpk]
    skill: Mapped[str] = mapped_column(String(255))

    created_at: Mapped[template_created_at]
    updated_at: Mapped[template_updated_at]

    __table_args__ = (
        UniqueConstraint('skill', name='skills_unique_skill'),
    )

    vacancies: Mapped[list["vacanciesModel"]] = relationship(
        secondary="skills_to_vacancy",
        back_populates="skills"
    )

class skills_to_vacancyModel(Base):
    __tablename__ = "skills_to_vacancy"

    id: Mapped[intpk]
    id_skill: Mapped[int] = mapped_column(ForeignKey("skills.id", ondelete="CASCADE", onupdate="CASCADE"))
    id_vacancy: Mapped[int] = mapped_column(ForeignKey("vacancies.id", ondelete="CASCADE", onupdate="CASCADE"))

    __table_args__ = (
        UniqueConstraint('id_skill', 'id_vacancy', name='skills_to_vacancy_unique_id_skill_id_vacancy'),
    )

    skill: Mapped["skillsModel"] = relationship(
        "skillsModel",
        overlaps="skills,vacancies"
    )
    vacancy: Mapped["vacanciesModel"] = relationship(
        "vacanciesModel",
        overlaps="skills,vacancies"
    )


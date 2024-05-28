from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    LOG_LEVEL: Literal["INFO"]

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str

    DB_NAME: str

    REDIS_HOST: str
    REDIS_PORT: int



    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def DATABASE_URL_SYNC(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
print(settings.DATABASE_URL)


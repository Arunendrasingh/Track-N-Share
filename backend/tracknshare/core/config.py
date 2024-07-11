from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    # DATABASE_URL: str = "postgresql://user:password@localhost:5432/tracknshare"

    class Config:
        env_file = ".env"


settings = Settings()

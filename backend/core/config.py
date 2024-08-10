from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    model_config = SettingsConfigDict(
        # `.env.prod` takes priority over `.env`
        env_file=('.env', '.env.prod'),
        extra="allow"
    )

    # class Config:
    #     env_file = ".env"


settings = Settings()

print(settings.API_V1_STR)
# DATABASE_URL: str = "postgresql://user:password@localhost:5432/tracknshare"

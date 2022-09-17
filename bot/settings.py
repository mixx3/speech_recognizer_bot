from pydantic import BaseSettings, PostgresDsn, AnyHttpUrl
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings"""

    BOT_TOKEN: str

    class Config:
        """Pydantic BaseSettings config"""

        case_sensitive = True
        env_file = ".env"


@lru_cache()
def get_settings():
    settings = Settings()
    return settings

from dynaconf import Dynaconf
from pydantic import BaseModel


class AppConfig(BaseModel):
    app_version: str
    app_name: str
    app_host: str
    app_port: int
    app_mount: str


class DBConfig(BaseModel):
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int

    @property
    def url(self):
        path = 'postgresql+asyncpg://{0}:{1}@{2}:{3}/{4}'.format(
            self.db_user,
            self.db_password,
            self.db_host,
            self.db_port,
            self.db_name
        )
        return path


class Settings(BaseModel):
    app: AppConfig
    db: DBConfig


dyna_settings = Dynaconf(
    settings_files=['settings.toml']
)

settings = Settings(
    app=dyna_settings['student-office-settings'],
    db=dyna_settings['db_settings']
)
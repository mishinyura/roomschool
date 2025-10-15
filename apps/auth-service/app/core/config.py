from pydantic import BaseModel
from dynaconf import Dynaconf


class AppConfig(BaseModel):
    debug: bool
    app_version: str
    app_name: str
    app_description: str
    app_host: str
    app_port: int
    app_mount: str
    app_key: str


class DBConfig(BaseModel):
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int

    @property
    def get_url(self):
        path = 'postgresql+asyncpg://{0}:{1}@{2}:{3}/{4}'.format(
            self.db_user,
            self.db_password,
            self.db_host,
            self.db_port,
            self.db_name
        )
        return path


class AuthConfig(BaseModel):
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int


class Settings(BaseModel):
    app: AppConfig
    db: DBConfig
    auth: AuthConfig


dyna_settings = Dynaconf(
    settings_files=["settings.toml"]
)

settings = Settings(
    app=dyna_settings["app_settings"],
    db=dyna_settings["db_settings"],
    auth=dyna_settings["auth_settings"]
)
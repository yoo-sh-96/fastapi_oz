from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from app.configs import config

TORTOISE_APP_MODELS = [  # tortoise에 의해서 사용되는 ORM 모델들은 전부 한곳에 등록해줘야 함.
    "app.tortoise_models.meeting",
    "aerich.models",
]

TORTOISE_ORM = {
    "connections": {  # 데이터베이스 연결 관련 설정들
        "default": {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": config.MYSQL_HOST,
                "port": config.MYSQL_PORT,
                "user": config.MYSQL_USER,
                "password": config.MYSQL_PASSWORD,
                "database": config.MYSQL_DB,
                "connect_timeout": config.MYSQL_CONNECT_TIMEOUT,
                "maxsize": config.CONNECTION_POOL_MAXSIZE,
            },
        },
    },
    "apps": {  # tortoise 관련 설정들
        "models": {"models": TORTOISE_APP_MODELS},
    },
    "timezone": "Asia/Seoul",
}


def initialize_tortoise(app: FastAPI) -> None:
    Tortoise.init_models(TORTOISE_APP_MODELS, "models")
    register_tortoise(app, config=TORTOISE_ORM)

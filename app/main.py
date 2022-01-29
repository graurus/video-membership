from fastapi import FastAPI
from . import config

main_app = FastAPI()
settings = config.get_settings()


@main_app.get("/")
def homepage():
    return {
        "helo": "WWWWWW",
        "keyspace": settings.keyspace,
        # "db_id": settings.db_client_id,
        # "db_secret": settings.db_client_secret,
    }  # json data -> REST API

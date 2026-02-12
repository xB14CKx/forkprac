from fastapi import FastAPI

# from .database.core import engine, Base

# import models here

#
from .api import register_routes
from .logging import configure_logging, LogLevels

configure_logging(log_level=LogLevels.info)

app = FastAPI()

# Base.metadata.create_all(engine)

register_routes(app=app)


@app.get("/")
def home():
    return {
        "message": "Hello World! This is the home page of the API. Please visit /docs to see the API documentation."
    }

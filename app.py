from fastapi import FastAPI
from endpoints import hello_world

__all__ = [
    "create_app",
]


def create_app(*args, **kwargs):
    app = FastAPI(*args, **kwargs)
    app.include_router(hello_world.router)

    return app

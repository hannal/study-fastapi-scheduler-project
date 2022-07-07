from fastapi import APIRouter

__all__ = ("router",)

router = APIRouter()


@router.get("/hello-world")
def hello():
    return "Hello World!"

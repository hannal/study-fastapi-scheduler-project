from fastapi import APIRouter

__all__ = ("router",)

router = APIRouter()


@router.get("/hello-world")
def hello():
    """hello world를 리턴합니다

    >>> hello()
    'Hello World!'
    """
    return "Hello World!"


def add_numbers(a: int, b: int) -> int:
    """숫자를 더합니다

    >>> add_numbers(1, 2)
    3
    """
    return a + b

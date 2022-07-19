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
    >>> add_numbers(3, 4)
    7
    >>> add_numbers(5, -4)
    1
    """
    return a + b


def only_numbers(a: int) -> int:
    """숫자만 입력받습니다.

    입력받은 숫자를 그대로 리턴합니다.
    >>> only_numbers(1)
    1

    ----
    숫자 이외의 입력을 받으면 `ValueError` 예외를 일으킵니다
    >>> only_numbers("1")
    Traceback (most recent call last):
        ...
    ValueError: Invalid value for a: '1'

    ----
    >>> only_numbers("a")
    Traceback (most recent call last):
        ...
    ValueError: ...

    ----
    아래 예제는 테스트하지 않습니다

    >>> only_numbers(1.0) # doctest: +SKIP
    ...
    """
    try:
        assert isinstance(a, int), f"Invalid value for a: {a}"
    except AssertionError as e:
        raise ValueError(e) from e
    return a

import pytest
from fastapi import FastAPI


@pytest.mark.skip
def test_create_app():
    from app import create_app

    app = create_app()
    assert isinstance(app, FastAPI)

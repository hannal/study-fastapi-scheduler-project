import sys
from pathlib import Path

sys.path.append(Path(__file__).resolve().parent.parent.as_posix())  # noqa

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app import create_app


@pytest.fixture
def app() -> FastAPI:
    return create_app()


@pytest.fixture
def client(app) -> TestClient:
    with TestClient(
        app=app,
        base_url="http://testserver",
    ) as client:
        yield client

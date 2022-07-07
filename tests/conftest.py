import sys

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

sys.path.append("..")

from app import create_app  # noqa


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

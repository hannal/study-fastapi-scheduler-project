import sys
from datetime import datetime
from pathlib import Path

from repositories import UserRepository, CandidateRepository
from schemas import User, Candidate

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


@pytest.fixture
def user() -> User:
    return UserRepository.create_user(2)


@pytest.fixture
def host() -> User:
    return UserRepository.create_user(1)


@pytest.fixture
def candidate() -> Candidate:
    CandidateRepository.create()
    return Candidate(id=1, when=datetime.now())

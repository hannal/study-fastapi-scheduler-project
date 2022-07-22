import datetime
import typing as t
from collections import defaultdict

import pydantic


class User(pydantic.BaseModel):
    id: int


class Candidate(pydantic.BaseModel):
    id: int
    when: datetime.datetime


class Event(pydantic.BaseModel):
    id: int
    host: User
    candidates: t.List[Candidate]


class CandidatePayload(pydantic.BaseModel):
    when: datetime.datetime


class CandidateVotePayload(pydantic.BaseModel):
    candidate_ids: list


fake_db = {
    'users': {
        1: User(id=1),
    },
    'events': defaultdict(dict),
    'candidate': defaultdict(dict),
    'attendance': defaultdict(dict),
}


class BaseError(Exception):
    pass


class ObjectNotExistError(BaseError):
    pass


class UserRepository:
    @classmethod
    def get_user(cls, user_id: int) -> User:
        if user := fake_db['users'].get(user_id):
            return User(**user)
        raise ObjectNotExistError


class EventRepository:
    @classmethod
    def get_event(cls, event_id: int) -> Event:
        if event := fake_db['events'].get(event_id):
            return Event(**event)
        raise ObjectNotExistError


class CandidateRepository:
    @classmethod
    def create(cls, event: Event, payload: CandidatePayload) -> Candidate:
        candidate = Candidate(id=1, **payload.dict())
        fake_db['candidate'][candidate.id] = candidate.dict()
        fake_db['events'][event.id] = event.dict()
        fake_db['events'][event.id]['candidates'].append(candidate)
        return candidate


def service_create_candidate(
        event: Event,
        candidate: CandidatePayload,
        candidate_repository: t.Type[CandidateRepository],
) -> Candidate:
    return candidate_repository.create(event, candidate)

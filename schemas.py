import datetime
import typing as t

import pydantic


class User(pydantic.BaseModel):
    id: int


class Candidate(pydantic.BaseModel):
    id: int
    when: datetime.datetime


class Attendance(pydantic.BaseModel):
    user: User
    candidate: Candidate


class Event(pydantic.BaseModel):
    id: int
    host: User
    candidates: t.List[Candidate]
    attendances: t.List[Attendance]


class CandidatePayload(pydantic.BaseModel):
    when: datetime.datetime


class CandidateVotePayload(pydantic.BaseModel):
    candidate_ids: list

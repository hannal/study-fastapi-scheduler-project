import datetime
import typing as t

import pydantic


class User(pydantic.BaseModel):
    id: int

    class Config:
        orm_mode = True


class Candidate(pydantic.BaseModel):
    id: int
    when: datetime.datetime

    class Config:
        orm_mode = True


class Attendance(pydantic.BaseModel):
    user: User
    candidate: Candidate

    class Config:
        orm_mode = True


class Event(pydantic.BaseModel):
    id: int
    host: User
    candidates: t.List[Candidate]
    attendances: t.List[Attendance]

    class Config:
        orm_mode = True


class CandidatePayload(pydantic.BaseModel):
    when: datetime.datetime


class CandidateVotePayload(pydantic.BaseModel):
    candidate_ids: list

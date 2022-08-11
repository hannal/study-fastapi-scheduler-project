import datetime
from collections import defaultdict

import models
import schemas
from db import AsyncSession as Session, use_db, op


class BaseError(Exception):
    pass


class ObjectNotExistError(BaseError):
    pass


class DuplicatedUserError(BaseError):
    pass


class UserRepository:
    @classmethod
    async def get_user(cls, user_id: int) -> schemas.User:
        session: Session = use_db()

        stmt = op.select(models.User).where(models.User.id == user_id)

        result = await session.execute(stmt)
        try:
            user = result.scalar_one()
            return schemas.User.from_orm(**user.dict())
        except Exception as exc:
            raise ObjectNotExistError() from exc

    @classmethod
    async def create_user(cls, user: schemas.User) -> schemas.User:
        session: Session = use_db()
        new_user = models.User(**user.dict())

        async with session.begin():
            try:
                session.add(new_user)
                await session.commit()
            except Exception as exc:
                await session.rollback()
                raise DuplicatedUserError()

        return schemas.User.from_orm(new_user)


class EventRepository:
    @classmethod
    async def get_event(cls, event_id: int) -> schemas.Event:
        session: Session = use_db()

        stmt = op.select(models.Event).where(models.Event.id == event_id)

        result = await session.execute(stmt)
        try:
            event = result.scalar_one()
            return schemas.Event.from_orm(event)
        except Exception as exc:
            raise ObjectNotExistError() from exc

    @classmethod
    async def add_attendance(cls, event_id: int, user_id: int, candidate_id: int) -> schemas.Attendance:
        session: Session = use_db()

        new_attendance = models.Attendance(event_id=event_id, user_id=user_id, candidate_id=candidate_id)

        async with session.begin():
            try:
                session.add(new_attendance)
                await session.commit()
            except Exception as exc:
                await session.rollback()
                raise DuplicatedUserError() from exc

        return schemas.Attendance.from_orm(new_attendance)


class CandidateRepository:
    @classmethod
    def create(cls, event_id: int, when: datetime.datetime) -> schemas.Candidate:
        session: Session = use_db()
        new_candidate = models.Candidate(event_id=event_id, when=when)

        async with session.begin():
            try:
                session.add(new_candidate)
                await session.commit()
            except Exception as exc:
                await session.rollback()
                raise DuplicatedUserError()

        return schemas.Candidate.from_orm(new_candidate)

    @classmethod
    async def get_candidate(cls, candidate_id: int) -> schemas.Candidate:
        session: Session = use_db()
        stmt = op.select(models.Candidate).where(models.Candidate.id == candidate_id)

        result = await session.execute(stmt)
        try:
            candidate = result.scalar_one()
            return schemas.Candidate.from_orm(**candidate.dict())
        except Exception as exc:
            raise ObjectNotExistError() from exc


fake_db = {
    'users': defaultdict(dict),
    'events': defaultdict(dict),
    'candidate': defaultdict(dict),
    'attendance': defaultdict(dict),
}

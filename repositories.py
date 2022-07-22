from collections import defaultdict

from schemas import User, Event, CandidatePayload, Candidate, Attendance


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

    @classmethod
    def add_attendance(cls, event_id: int, user: User, candidate: Candidate) -> Event:
        event = cls.get_event(event_id)
        event.attendances.append(Attendance(user=user, candidate=candidate))
        fake_db['events'][event.id] = event.dict()
        return Event(**event)


class CandidateRepository:
    @classmethod
    def create(cls, event: Event, payload: CandidatePayload) -> Candidate:
        candidate = Candidate(id=1, **payload.dict())
        fake_db['candidate'][candidate.id] = candidate.dict()
        fake_db['events'][event.id] = event.dict()
        fake_db['events'][event.id]['candidates'].append(candidate)
        return candidate

    @classmethod
    def get_candidate(cls, candidate_id: int) -> Candidate:
        if candidate := fake_db['candidate'].get(candidate_id):
            return Event(**candidate)
        raise ObjectNotExistError



fake_db = {
    'users': {
        1: User(id=1),
    },
    'events': defaultdict(dict),
    'candidate': defaultdict(dict),
    'attendance': defaultdict(dict),
}

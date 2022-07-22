from datetime import datetime

import services.attendee
from repositories import fake_db, EventRepository
from schemas import User, Event, Candidate, Attendance


def test_vote_candidate_service():
    host = User(id=1)
    user = User(id=2)
    candidate = Candidate(id=1, when=datetime.now())
    event = Event(id=1, host=host, candidates=[candidate], attendances=[])
    fake_db["users"][2] = user.dict()
    fake_db["candidate"][1] = candidate.dict()
    fake_db["events"][1] = event.dict()

    # vote_candidate call
    services.attendee.vote_candidate(user, event, candidate)

    # event get
    event = EventRepository.get_event(event_id=event.id)

    # attendance check
    assert event.attendances[0] == Attendance(user=user, candidate=candidate)


def test_vote_create_endpoint():
    host = User(id=1)
    user = User(id=2)
    candidate = Candidate(id=1, when=datetime.now())
    event = Event(id=1, host=host, candidates=[candidate], attendances=[])
    fake_db["users"][2] = user.dict()
    fake_db["candidate"][1] = candidate.dict()
    fake_db["events"][1] = event.dict()

    class MockAttendeeRepository:
        @classmethod

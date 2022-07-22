import datetime

from services.candidate import service_create_candidate
from repositories import EventRepository, CandidateRepository
from schemas import User, Event, CandidatePayload


def test_service_create_candidate():
    user = User(id=1)
    event = Event(host=user, id=1, candidates=[])
    candidate_payload = CandidatePayload(when=datetime.datetime(2022, 7, 22))
    obj = service_create_candidate(event, candidate_payload, CandidateRepository)
    assert isinstance(obj.id, int)

    event2 = EventRepository.get_event(event.id)
    assert all([True for _o in event2.candidates if _o.id == obj.id])

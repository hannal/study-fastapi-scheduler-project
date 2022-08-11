import datetime
from unittest.mock import MagicMock

from services import candidate
from services.candidate import service_create_candidate
from repositories import EventRepository, CandidateRepository
from schemas import User, Event, CandidatePayload


def test_create_candidate(client, monkeypatch):
    user = User(id=1)
    event = Event(host=user, id=1, candidates=[], attendances=[])

    class MockEventRepository:
        @classmethod
        def get_event(cls, *args, **kwargs):
            return event

    url = f'/{event.id}/candidate'
    response = client.get(url)
    assert response.status_code == 404

    mock = MagicMock()
    mock.return_value = MockEventRepository

    with monkeypatch.context() as m:
        m.setattr(candidate, "EventRepository", mock)
        when = datetime.datetime.now()
        expected = when.isoformat()
        params = {'when': expected}
        response = client.post(url, json=params)
        assert response.status_code == 200
        assert response.json()['when'] == expected

    # user = User(id=1)
    # event = Event(host=user, id=1, candidates=[])
    # candidate_payload = CandidatePayload(when=datetime.datetime(2022, 7, 22))
    # obj = service_create_candidate(event, candidate_payload, CandidateRepository)
    # assert isinstance(obj.id, int)
    #
    # event2 = EventRepository.get_event(event.id)
    # assert all([True for _o in event2.candidates if _o.id == obj.id])

import datetime

from services.candidate import EventRepository, CandidateRepository, service_create_candidate, User, Event, \
    CandidatePayload


def test_create_candidate(client):
    user = User(id=1)
    event = Event(host=user, id=1, candidates=[])

    response = client.get('/1/candidate')
    assert response.status_code == 404

    params = {'when': '2022-07-15T12:25:00Z'}
    response = client.post('/1/candidate', json=params)
    assert response.status_code == 200
    assert response.json()['when'] == '2022-07-15T12:25:00Z'

    # user = User(id=1)
    # event = Event(host=user, id=1, candidates=[])
    # candidate_payload = CandidatePayload(when=datetime.datetime(2022, 7, 22))
    # obj = service_create_candidate(event, candidate_payload, CandidateRepository)
    # assert isinstance(obj.id, int)
    #
    # event2 = EventRepository.get_event(event.id)
    # assert all([True for _o in event2.candidates if _o.id == obj.id])

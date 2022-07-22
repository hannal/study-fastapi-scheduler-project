from fastapi import APIRouter, Body, Depends
from fastapi import status
from fastapi.exceptions import HTTPException

from services.candidate import service_create_candidate
from repositories import ObjectNotExistError, UserRepository, EventRepository, CandidateRepository, fake_db
from schemas import User, Event, CandidatePayload, CandidateVotePayload

router = APIRouter()


def use_user():
    try:
        return UserRepository.get_user(user_id=1)
    except ObjectNotExistError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


def use_event(event_id: str) -> Event:
    try:
        return EventRepository.get_event(event_id=event_id)
    except ObjectNotExistError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.post('/{event_id}/candidate')
def create_candidate(
        event: Event = Depends(use_event),
        candidate: CandidatePayload = Body(...),
        user: User = Depends(use_user)
):
    if event.host.id != user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return service_create_candidate(event=event, candidate=candidate, candidate_repository=CandidateRepository)


@router.get('/{event_id}/candidates/')
def list_candidates(event: Event = Depends(use_event)):
    # get event

    if event.id not in fake_db['events']:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    event = fake_db['events'][event.id]
    return event['candidates']
    # return candidates


@router.post('/{event_id}/candidates/vote/')
def vote_candidate(
        event_id: int,
        candidate_ids: CandidateVotePayload = Body(...),
        user: User = Depends(use_user)
):
    for candidate_id in candidate_ids:
        fake_db['attendance'][event_id][candidate_id].append(user.id)

    return {}

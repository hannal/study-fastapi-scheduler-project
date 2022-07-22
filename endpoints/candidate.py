from fastapi import APIRouter, Body, Depends
from fastapi import status
from fastapi.exceptions import HTTPException

import services.attendee
from services.candidate import service_create_candidate
from repositories import ObjectNotExistError, UserRepository, EventRepository, CandidateRepository, fake_db
from schemas import User, Event, CandidatePayload, CandidateVotePayload, Candidate

router = APIRouter()


def use_user():
    try:
        return UserRepository.get_user(user_id=1)
    except ObjectNotExistError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


def use_candidate_ids(candidate_ids):
    if not candidate_ids:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    candidates = []
    try:
        for candidate_id in candidate_ids:
            candidates.append(CandidateRepository.get_candidate(candidate_id=candidate_id))
    except ObjectNotExistError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return candidates


def use_event(event_id: int) -> Event:
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
        event: Event = Depends(use_event),
        candidates: list[Candidate] = Depends(use_candidate_ids),
        user: User = Depends(use_user)
):
    for candidate in candidates:
        services.attendee.vote_candidate(user, event, candidate)

    return EventRepository.get_event(event.id)

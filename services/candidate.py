import typing as t

from repositories import CandidateRepository
from schemas import Candidate, Event, CandidatePayload


def service_create_candidate(
        event: Event,
        candidate: CandidatePayload,
        candidate_repository: t.Type[CandidateRepository],
) -> Candidate:
    return candidate_repository.create(event, candidate)

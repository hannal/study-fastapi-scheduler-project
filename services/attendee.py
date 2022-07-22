import typing as t
from dataclasses import dataclass

from starlette import status

from repositories import EventRepository
from schemas import User, Event, Candidate


@dataclass
class ServiceReturnResult:
    result: int
    data: t.Optional[t.Any] = None


def vote_candidate(user: User, event: Event, candidate: Candidate) -> ServiceReturnResult:
    # 이용자가 동일한 후보일정에 중복 투표하지 않도록 처리.
    ## 기존 이벤트의 candidates 에서 현 이용자가 투표한 것이 있는지 검사
    if any(filter(lambda o: o.user.id == user.id, event.attendances)):
        return ServiceReturnResult(result=status.HTTP_200_OK, data=event)

    # 해당 이벤트에 대한 갱신된 데이터, 결과 반환
    event = EventRepository.add_attendance(event.id, user, candidate)
    return ServiceReturnResult(result=status.HTTP_201_CREATED, data=event)

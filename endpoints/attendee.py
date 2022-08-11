from fastapi import APIRouter, Body, Depends
from fastapi import status
from fastapi.exceptions import HTTPException

from services.candidate import service_create_candidate
from repositories import ObjectNotExistError, UserRepository, EventRepository, CandidateRepository, fake_db
from schemas import User, Event, CandidatePayload, CandidateVotePayload

router = APIRouter()


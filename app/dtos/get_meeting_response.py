from __future__ import annotations

from datetime import date

from pydantic import BaseModel

from app.dtos.frozen_config import FROZEN_CONFIG
from app.tortoise_models.meeting import MeetingModel


class ParticipantDateResponse(BaseModel):
    model_config = FROZEN_CONFIG
    date: date
    enabled: bool
    starred: bool
    id: int


class ParticipantResponse(BaseModel):
    model_config = FROZEN_CONFIG
    id: int
    name: str
    dates: list[ParticipantDateResponse]


class GetMeetingResponse(BaseModel):
    model_config = FROZEN_CONFIG

    url_code: str
    start_date: date | None = None
    end_date: date | None = None
    title: str
    location: str
    participants: list[ParticipantResponse]

    @classmethod
    def from_mysql(cls, meeting: MeetingModel) -> GetMeetingResponse:
        return GetMeetingResponse(
            url_code=meeting.url_code,
            end_date=meeting.end_date,
            start_date=meeting.start_date,
            title=meeting.title,
            location=meeting.location,
            participants=[
                ParticipantResponse(
                    id=p.id,
                    name=p.name,
                    dates=[
                        ParticipantDateResponse(date=pd.date, id=pd.id, enabled=pd.enabled, starred=pd.starred)
                        for pd in p.participant_dates
                    ],
                )
                for p in meeting.participants
            ],
        )

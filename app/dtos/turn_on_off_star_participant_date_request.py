import uuid

from pydantic import BaseModel


class TurnOnOffStarParticipantDateRequestEdgedb(BaseModel):
    participant_date_id: uuid.UUID
    meeting_url_code: str


class TurnOnOffStarParticipantDateRequestMysql(BaseModel):
    participant_date_id: int
    meeting_url_code: str

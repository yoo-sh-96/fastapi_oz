from __future__ import annotations

import datetime

from tortoise import Model, fields

from app.dtos.update_meeting_request import MEETING_DATE_MAX_RANGE
from app.tortoise_models.base_model import BaseModel
from app.tortoise_models.participant import ParticipantModel


class ParticipantDateModel(BaseModel, Model):
    participant: fields.ForeignKeyRelation[ParticipantModel] = fields.ForeignKeyField(
        "models.ParticipantModel", related_name="participant_dates", db_constraint=False
    )
    date = fields.DateField()
    enabled = fields.BooleanField(default=True)
    starred = fields.BooleanField(default=False)

    class Meta:
        table = "participant_dates"

    @classmethod
    async def bulk_create_participant_date(cls, participant_id: int, dates: list[datetime.date]) -> None:
        await cls.bulk_create([ParticipantDateModel(participant_id=participant_id, date=date) for date in dates])

    @classmethod
    async def get_all_by_participant_id(cls, participant_id: int) -> list[ParticipantDateModel]:
        return (
            await ParticipantDateModel.filter(participant_id=participant_id)
            .limit(MEETING_DATE_MAX_RANGE.days)
            .order_by("date")
            .all()
        )

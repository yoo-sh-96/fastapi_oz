from __future__ import annotations

import datetime

from tortoise import Model, fields

from app.dtos.update_meeting_request import MEETING_DATE_MAX_RANGE
from app.tortoise_models.base_model import BaseModel
from app.tortoise_models.participant import ParticipantModel


class ParticipantDateModel(BaseModel, Model):
    # 수정! index 추가
    participant: fields.ForeignKeyRelation[ParticipantModel] = fields.ForeignKeyField(
        "models.ParticipantModel", related_name="participant_dates", db_constraint=False, index=True
    )
    date = fields.DateField()
    enabled = fields.BooleanField(default=True)
    starred = fields.BooleanField(default=False)

    class Meta:
        table = "participant_dates"

    @classmethod
    async def bulk_create_participant_dates(cls, participant_id: int, dates: list[datetime.date]) -> None:
        await cls.bulk_create([ParticipantDateModel(participant_id=participant_id, date=date) for date in dates])

    @classmethod
    async def get_all_by_participant_id(cls, participant_id: int) -> list[ParticipantDateModel]:
        return (
            await ParticipantDateModel.filter(participant_id=participant_id)
            .limit(MEETING_DATE_MAX_RANGE.days)
            .order_by("date")
            .all()
        )

    @classmethod
    async def on(cls, participant_date_id: int) -> None:
        await cls.filter(id=participant_date_id).update(enabled=True)

    @classmethod
    async def off(cls, participant_date_id: int) -> None:
        await cls.filter(id=participant_date_id).update(enabled=False, starred=False)

    @classmethod
    async def star(cls, participant_date_id: int) -> None:
        await cls.filter(id=participant_date_id).update(enabled=True, starred=True)

    @classmethod
    async def unstar(cls, participant_date_id: int) -> None:
        await cls.filter(id=participant_date_id).update(starred=False)

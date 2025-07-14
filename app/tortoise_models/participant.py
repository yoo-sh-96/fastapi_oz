from __future__ import annotations

from tortoise import Model, fields

from app.tortoise_models.base_model import BaseModel
from app.tortoise_models.meeting import MeetingModel


class ParticipantModel(BaseModel, Model):
    name = fields.CharField(max_length=255)
    meeting: fields.ForeignKeyRelation[MeetingModel] = fields.ForeignKeyField(
        "models.MeetingModel",
        related_name="participants",
        db_constraint=False,
        on_delete=fields.CASCADE,
        to_field="url_code",
        # db 에는 meeting_id 로 생성됩니다. 이걸 컨트롤하는 방법을 제공하지 않습니다 ㅠㅠ
        # https://tortoise.github.io/fields.html?h=foreignkey
    )
    meeting_id: str

    class Meta:
        table = "participants"

    @classmethod
    async def create_participant(cls, name: str, meeting_url_code: str) -> ParticipantModel:
        return await cls.create(name=name, meeting_id=meeting_url_code)

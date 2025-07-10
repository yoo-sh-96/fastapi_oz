from fastapi import APIRouter

from app.dtos.create_meeting_response import CreateMeetingResponse
from app.service.meeting_service_mysql import service_create_meeting_mysql

edgedb_router = APIRouter(prefix="/v1/edgedb/meetings", tags=["Meeting"])
mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["Meeting"])

# 원래는 어떤 디비를 쓰는지 URL에 적을 필요가 없다
# 강의에서만 이렇게 합니다!
# 실전에서는 db이름을 url에 넣지 말자!


@edgedb_router.post("", description="meeting을 생성합니다")
async def api_create_meeting_edgedb() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")


@mysql_router.post("", description="meeting을 생성합니다.")
async def api_create_meeting_mysql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code=(await service_create_meeting_mysql()).url_code)

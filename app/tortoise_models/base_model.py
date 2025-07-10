from tortoise import fields


class BaseModel:
    id = fields.BigIntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)


# MySQL: PK를 정할 때 주의해야 되는점
# MySQL 버전 8이상 부터라면
# innidb가 디폴트 엔진

# innodb의 특징 중 하나 -> clustering index
# primary key를 기준으로 pk값이 비슷한 row들 끼리 disk에서도 실제로 모여있다.

# HDD
# 랜덤 IO가 느리고, 순차 IO가 빠르다.

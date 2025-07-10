# import timeit
# import uuid
# from typing import Sequence
# from datetime import datetime
#
# from sqids import  sqids
#
# from app.utils.base62 import Base62
#
# squid = sqids.Sqids()
#
# class Squids:
#
#     @classmethod
#     def encode(cls, nums: Sequence[int]) -> str:
#         return squid.encode(nums)
#
#
# def do_squids():
#     now = datetime.now()
#     return Squids.encode(
#         [now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond]
#     )
#
# def do_base62():
#     uu = uuid.uuid4()
#     return Base62.encode(uu.int)
#
# if __name__ == '__main__':
#     print(timeit.timeit(lambda: do_squids(), number=100000))
#     print(timeit.timeit(lambda: do_base62(), number=100000))

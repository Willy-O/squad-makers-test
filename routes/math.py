# from math import lcm
from math import gcd

from fastapi import APIRouter, Query

router = APIRouter(
  prefix="/math",
)

@router.get("/plus-one")
async def plus_one_to_current_number(number: int = Query(...)):
  new_number = number + 1
  return {
    "detail": "success",
    "message": "return the number sent whit plus '1'",
    "result": new_number
  }

@router.get("/lcm")
async def least_commom_multiple(numbers: list[int] = Query(...)):
  lcm = 1
  for number in numbers:
    lcm = lcm * number // gcd(lcm, number)
  return {
    "detail": "success",
    "message": "return last common multiple the list sent",
    "result": lcm
  }

from fastapi import APIRouter, Query

router = APIRouter(
  prefix="/math",
)

@router.get("/plus-one")
async def sum_one_to_current_number(number: int = Query(...)):
  new_number = number + 1
  return {
    "detail": "success",
    "result": new_number
  }

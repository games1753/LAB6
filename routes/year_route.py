from asyncio.windows_events import NULL
from fastapi import APIRouter
import datetime
x = datetime.datetime.now()
courses_api_router = APIRouter()


@courses_api_router.get("/service/getage")
async def read_item(year: int):
    if year != 0:
        if year < 0:
            return {"msg":"Negative numbers cannot be entered"}
        elif year > (x.year+543):
            return {"msg":"That's the future"}
        else :
            year = (x.year+543)-year
            return {"age": year}
    return {"msg": "Can't find age if you enter a zero."}
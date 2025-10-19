from app.model.echo import EchoResponse
from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/echo", response_model=EchoResponse)
async def echo_memo(request: Request):
    data = await request.json()
    print(data)
    return EchoResponse(**data)

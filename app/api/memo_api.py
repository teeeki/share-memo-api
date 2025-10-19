from app.model.memo_model import MemoModel
from app.model.echo import EchoResponse
from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/memo/")
async def create_memo(request: Request, response_model=MemoModel):
    data = await request.json()
    print(data)
    return MemoModel(**data)

# あとでかえる
@router.get("/memo/", response_model=EchoResponse)
async def get_memo():
    return EchoResponse(message="Here is your memo")

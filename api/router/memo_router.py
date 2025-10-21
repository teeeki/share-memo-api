from typing import List
from api.schema.memo_schema import MemoModel
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Hello from FastAPI backend!"}

@router.post("/memo/")
async def create_memo():
    pass


@router.get("/memo/", response_model=List[MemoModel], tags=["memo"])
async def get_memo():
    return [MemoModel(user_id=1, title="サンプル", summary="サンプルsummary", content="サンプルcontent")]
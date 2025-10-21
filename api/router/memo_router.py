from typing import List
from api.schema.memo_schema import MemoModel
from api.service import memo_service
from fastapi import APIRouter

router = APIRouter()


@router.post("/memo")
async def create_memo():
    pass


@router.get("/memo", response_model=List[MemoModel], tags=["memo"])
async def get_memo():
    
    result = memo_service.get_memos()
    return [MemoModel(**memo) for memo in result]
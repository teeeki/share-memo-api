from typing import List
from api.schema.memo_schema import MemoResponse
from api.service import memo_service
from fastapi import APIRouter, Depends, Query
from api.config.db_setting import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/create-memo")
async def create_memo():
    pass


@router.get("/get-memo", response_model=List[MemoResponse], tags=["memo"])
async def get_memo(user_id: List[int]=Query(None), session: Session = Depends(get_db)):
    result = memo_service.get_memos(session, user_id=user_id)
    return [MemoResponse(**memo) for memo in result]
from typing import List
from api.schema.memo_schema import MemoModel
from api.service import memo_service
from fastapi import APIRouter, Depends
from api.config.db_setting import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/memo")
async def create_memo():
    pass


@router.get("/memo", response_model=List[MemoModel], tags=["memo"])
async def get_memo(session: Session = Depends(get_db)):
    result = memo_service.get_memos(session)
    return [MemoModel(**memo) for memo in result]
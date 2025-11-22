from typing import List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.schemas.memo import MemoResponse
from app.services.memo import get_memos
from app.config.database import get_db

router = APIRouter()


@router.post("/create-memo")
async def create_memo():
    pass


@router.get("/get-memos", response_model=List[MemoResponse], tags=["memo"])
async def get_memos_endpoint(
    user_id: List[int] = Query(None), 
    session: Session = Depends(get_db)
):
    result = get_memos(session, user_id=user_id)
    return [MemoResponse(**memo) for memo in result]


from typing import List
from sqlalchemy.orm import Session
from app.crud.memo import MemoCRUD

def get_memos(session: Session, user_id: int | List[int] | None = None):
    result = MemoCRUD.get_memos_by_user_ids(session, user_id=user_id)
    return result


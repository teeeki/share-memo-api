from api.config.db_setting import get_db
from api.crud.memo_crud import MemoCRUD
from fastapi import Depends

def get_memos(session = Depends(get_db)):
    
    result = MemoCRUD.get_memos_by_user_ids(session, user_ids=[1,2,3])
    return result
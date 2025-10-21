from pydantic import BaseModel

class MemoModel(BaseModel):
    user_id: int
    title: str
    summary: str
    content: str
    
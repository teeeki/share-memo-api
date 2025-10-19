from pydantic import BaseModel

class MemoModel(BaseModel):
    title: str
    user: str
    summary: str
    content: str
    
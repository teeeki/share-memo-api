from pydantic import BaseModel
from typing import Any, Dict

class Memo(BaseModel):
    title: str
    content: str
    
class EchoResponse(BaseModel):
    user: str
    memos: list[Memo]
from pydantic import BaseModel

# memoのレスポンスモデル
class MemoResponse(BaseModel):
    user_id: int
    title: str
    summary: str
    content: str
    
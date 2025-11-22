from pydantic import BaseModel

# memoのレスポンスモデル
class MemoResponse(BaseModel):
    username: str
    title: str
    summary: str
    content: str


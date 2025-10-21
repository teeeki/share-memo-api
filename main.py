from fastapi import FastAPI
from api.router import memo_router

app = FastAPI()

app.include_router(memo_router.router, prefix="/api", tags=["memos"])
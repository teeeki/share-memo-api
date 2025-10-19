from fastapi import FastAPI
from app.api import echo, memo_api

app = FastAPI()

app.include_router(echo.router, prefix="/api", tags=["memos"])
app.include_router(memo_api.router, prefix="/api", tags=["memos"])

@app.get("/")
def root():
    return {"message": "Hello from FastAPI backend!"}
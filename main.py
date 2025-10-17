from fastapi import FastAPI
from app.api import echo

app = FastAPI()

app.include_router(echo.router, prefix="/api", tags=["memos"])

@app.get("/")
def root():
    return {"message": "Hello from FastAPI backend!"}
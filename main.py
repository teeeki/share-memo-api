from fastapi import FastAPI
from api.router import memo_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI backend!"}

app.include_router(memo_router.router, prefix="/api", tags=["memos"])
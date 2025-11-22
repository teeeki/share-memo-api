from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import memos

app = FastAPI()

# 開発用 CORS（本番では allow_origins を限定すること）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # 例: ["http://localhost:3000"] に限定するのが安全
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello from FastAPI backend!"}

app.include_router(memos.router, prefix="/api", tags=["memos"])
from fastapi import FastAPI

app = FastAPI()

# 仮のメモデータ
memos = [
    {"id": 1, "title": "買い物リスト", "content": "卵、牛乳、パン"},
    {"id": 2, "title": "やること", "content": "洗濯、掃除、読書"},
]

@app.get("/memos")
def get_memos():
    return {"memos": memos}

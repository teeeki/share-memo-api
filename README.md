# メモ共有アプリのAPI

## 環境構築
- python仮想環境の作成と有効化（PowerShell）
```bash
python -m venv share-memo
./share-memo/Scripts/activate
``` 

※ 仮想環境有効化に失敗した場合、PowerShellの実行ポリシーを変更する必要がある  
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

## FastAPIのインストール
```bash
pip install fastapi uvicorn
```

## FastAPIの起動
```bash
uvicorn main:app --reload
``` 
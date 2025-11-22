from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import Any

class RawCRUD:
    @classmethod
    def fetchall(cls, session: Session, query: str, prm: dict[str, Any] | None = None):
        result = session.execute(text(query), prm)
        return [dict(row) for row in result.mappings().fetchall()]


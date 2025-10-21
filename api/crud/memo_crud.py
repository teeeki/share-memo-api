from sqlalchemy.orm import Session
from .base_crud import RawCRUD

class MemoCRUD:
    @classmethod
    def get_memos_by_user_ids(cls, session: Session, user_ids: list[int]):
        query = """
            SELECT
                u.user_id,
                m.title,
                m.summary,
                m.content
            FROM
                users u
            INNER JOIN
                memos m ON u.user_id = m.user_id
            WHERE
                u.user_id = ANY(:user_ids)
        """
        return RawCRUD.fetchall(session, query, {"user_ids": user_ids})

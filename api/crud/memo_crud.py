from sqlalchemy.orm import Session
from crud_base import RawCRUD

class MemoCRUD:
    @classmethod
    def get_memos_by_user_ids(cls, session: Session, user_ids: list[int]):
        query = """
            SELECT
                u.id AS user_id,
                u.name AS user_name,
                m.id AS memo_id,
                m.title,
                m.content,
                m.created_at
            FROM
                users u
            LEFT JOIN
                memos m ON u.id = m.user_id
            WHERE
                u.id = ANY(:user_ids)
            ORDER BY
                u.id, m.created_at DESC
        """
        return RawCRUD.fetchall(session, query, {"user_ids": user_ids})

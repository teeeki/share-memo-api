from sqlalchemy.orm import Session
from .base import RawCRUD

class MemoCRUD:
    @classmethod
    def get_memos_by_user_ids(cls, session: Session, user_id: list[int] | None = None):
        base_query = """
            SELECT
                u.username,
                m.title,
                m.summary,
                m.content
            FROM
                users u
            INNER JOIN
                memos m ON u.user_id = m.user_id
        """
        
        # user_idが指定されている場合はuser_idで絞り込む
        if user_id:
            query = base_query + """
            WHERE
                u.user_id = ANY(:user_id)
            """
        else:
            query = base_query

        return RawCRUD.fetchall(session, query, {"user_id": user_id})


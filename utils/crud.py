from dbs.db import LocalSession
from dbs.models import Quest

def save_quests(subject: str, level: str, question: str) -> int:
    db = LocalSession()
    q = Quest(
        subject = subject,
        level = level,
        question = question
    )
    db.add(q)
    db.commit()
    db.refresh(q)
    db.close()
    return q.id

def get_question(qna_id: int) -> str | None:
    db = LocalSession()
    q = db.query(Quest).filter(Quest.id == qna_id).first()
    db.close()
    return q.question if q else None

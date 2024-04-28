
from sqlalchemy.orm import Session
from api.models.tmykQuestion import TMYKQuestions
def get_tmyk_questions(db: Session, id: int):
    result = db.query(TMYKQuestions).filter()
    return [res.__dict__ for res in result]
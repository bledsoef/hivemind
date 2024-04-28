
from sqlalchemy.orm import Session
from api.models.tmyk.question import Question
from api.models.tmyk.game import Game
from api.models.user import User
def get_tmyk_questions(db: Session, id: int):
    result = db.query(Question).filter(Game.id == Question.game_id)
    return [res.__dict__ for res in result]

def get_tmyk_games(db: Session):
    return [
        dict(game=game.__dict__, user=user.__dict__) for game, user in (
            db.query(Game, User).join(User, Game.user_id == User.username, isouter=True).all()
            )
        ]
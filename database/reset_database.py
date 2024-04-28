from database.config import Base, engine
from sqlalchemy.orm import Session

from api.models.tmyk.game import Game
from api.models.tmyk.question import Question
from api.models.user import User

from datetime import datetime

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
with Session(engine) as session:
    user1 = User(username="bledsoef", email="bledsoef", first_name="Finn", last_name="Bledsoe")
    session.add_all([user1])
    session.commit()

    game1 = Game(id=1, name="Test", user_id=user1.username)
    session.add_all([game1])
    session.commit()

    question1 = Question(game_id=1, question="Who is the famous person?", valid_answers="[Finn Bledsoe]")
    question2 = Question(game_id=1, question="Who is the famous person?", valid_answers="[Finn Bledsoe Again!]")
    
    session.add_all([question1, question2])
    session.commit()
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from database.config import get_db
from api.logic.tmyk import get_tmyk_questions, get_tmyk_games

router = APIRouter()

@router.get("/api/getQuestions")
async def getQuestions(id: int, db: Session = Depends(get_db)):
    questions = get_tmyk_questions(db, id)
    return questions

@router.get("/api/getGames")
async def getGames(db: Session = Depends(get_db)):
    questions = get_tmyk_games(db)
    return questions
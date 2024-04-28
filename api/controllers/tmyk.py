from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from database.config import get_db
from api.logic.tmyk import get_tmyk_questions
router = APIRouter()

@router.get("/getQuestions")
async def getQuestions(id: int, db: Session = Depends(get_db)):
    questions = get_tmyk_questions(db, id)
    return questions
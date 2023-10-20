from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated

import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

from starlette.responses import RedirectResponse

app = FastAPI()
models.Base.metadata.create_all(bind=engine) #esta linea crea toda las tablas en nuestra BD


class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool

class QuestionBase(BaseModel):
    question_text: str
    choice: List[ChoiceBase]

class QuestionUpdate(BaseModel):
    question_text: str

    class config:
        orm_mode = True

def get_db():           #tratamos de hacer una conexion con nuestra BD
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get('/')
async def home():
    return RedirectResponse(url="/docs/")

@app.get('/questions/')
async def get_questions(db: db_dependency):
    result = db.query(models.Question).all()
    if not result:
        raise HTTPException(status_code=404, detail="No se consiguieron datos")
    return result

@app.get('/questions/{question_id}')
async def get_question(question_id: int, db: db_dependency):
    result = db.query(models.Question).filter(models.Question.id == question_id).first()
    if not result:
        raise HTTPException(status_code=404, detail='No se consigio la pregunta')
    return result

@app.get('/choices/{questions_id}')
async def get_question(question_id: int, db: db_dependency):
    result = db.query(models.Choice).filter(models.Choice.question_id == question_id).all()
    if not result:
        raise HTTPException(status_code=404, detail='No se consigio la pregunta')
    return result

@app.post('/questions/')
async def create_questions(question: QuestionBase, db:db_dependency):
    db_question = models.Question(question_text=question.question_text)
    if not db_question:
        raise HTTPException(status_code=500, detail="No se pudo crear la pregunta")
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    for choice in question.choice:
        db_choice = models.Choice(choice_text = choice.choice_text, is_correct = choice.is_correct, question_id = db_question.id)  
        db.add(db_choice)
    db.commit()
    return {"mensaje":"Pregunta creada!"}

@app.put('/questions/{question_id}')
async def update_question(question_id:int, update: QuestionUpdate, db: db_dependency):
    question = db.query(models.Question).filter(models.Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail='No se encontró la pregunta')
    question.question_text = update.question_text
    db.commit()
    db.refresh(question)
    return question

@app.delete('/questions/{question_id}')
async def delete_question(question_id: int, db: db_dependency):
    question = db.query(models.Question).filter(models.Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail='No se consigio la pregunta')
    db.delete(question)
    db.commit()
    return {"mensaje":"Pregunta eliminada!"}
  

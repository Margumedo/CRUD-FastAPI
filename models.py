# Es donde van a estar mis funciones que van a trabajar con sqlalchemys y recuperar datos de la BD
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base
from sqlalchemy.orm import relationship


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, index=True)
    choices = relationship("Choice", back_populates="question", cascade="all, delete-orphan")

class Choice(Base):
    __tablename__ = "choice"

    id = Column(Integer, primary_key=True, index=True)
    choice_text = Column(String, index=True)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", back_populates="choices")

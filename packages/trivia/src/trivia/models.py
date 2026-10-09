import os

from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

database_name = os.environ.get("DATABASE_NAME", "trivia")
database_user = os.environ.get("DATABASE_USER", "postgres")
database_password = os.environ.get("DATABASE_PASSWORD", "postgres")
database_host = os.environ.get("DATABASE_HOST", "localhost:5432")
database_path = (
    f"postgresql://{database_user}:{database_password}@{database_host}/{database_name}"
)

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)


class Question(db.Model):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    category = Column(String, nullable=False)
    difficulty = Column(Integer, nullable=False)

    def __init__(self, question, answer, category, difficulty, id=None):
        self.question = question
        self.answer = answer
        self.category = category
        self.difficulty = difficulty
        if id is not None:
            self.id = id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "question": self.question,
            "answer": self.answer,
            "category": self.category,
            "difficulty": self.difficulty,
        }


class Category(db.Model):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)

    def __init__(self, type):
        self.type = type

    def format(self):
        return {"id": self.id, "type": self.type}

import unittest

from sqlalchemy.pool import StaticPool

from trivia import create_app
from trivia.models import Category, Question, db


class TriviaModelsTestCase(unittest.TestCase):
    """Unit tests for the Question and Category models."""

    TEST_CONFIG = {
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_ENGINE_OPTIONS": {
            "connect_args": {"check_same_thread": False},
            "poolclass": StaticPool,
        },
    }

    def setUp(self):
        self.app = create_app(self.TEST_CONFIG)
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
            db.engine.dispose()

    def test_question_format(self):
        q = Question(
            question="What is the capital of France?",
            answer="Paris",
            category=3,
            difficulty=1,
        )
        self.assertEqual(
            q.format(),
            {
                "id": None,
                "question": "What is the capital of France?",
                "answer": "Paris",
                "category": 3,
                "difficulty": 1,
            },
        )

    def test_question_insert_and_persistence(self):
        with self.app.app_context():
            q = Question(
                question="Hematology studies what?",
                answer="Blood",
                category=1,
                difficulty=4,
            )
            q.insert()
            self.assertIsNotNone(q.id)
            fetched = db.session.get(Question, q.id)
            self.assertEqual(fetched.question, "Hematology studies what?")
            self.assertEqual(fetched.answer, "Blood")

    def test_question_update(self):
        with self.app.app_context():
            q = Question(
                question="Original",
                answer="A",
                category=1,
                difficulty=1,
            )
            q.insert()
            q.difficulty = 5
            q.update()
            fetched = db.session.get(Question, q.id)
            self.assertEqual(fetched.difficulty, 5)

    def test_question_delete(self):
        with self.app.app_context():
            q = Question(
                question="To remove",
                answer="X",
                category=1,
                difficulty=1,
            )
            q.insert()
            q_id = q.id
            q.delete()
            self.assertIsNone(db.session.get(Question, q_id))

    def test_category_format(self):
        c = Category(type="Science")
        self.assertEqual(c.format(), {"id": None, "type": "Science"})

    def test_category_persists_independently(self):
        with self.app.app_context():
            c = Category(type="History")
            c.insert() if hasattr(c, "insert") else db.session.add(c)
            if not hasattr(c, "insert"):
                db.session.commit()
            self.assertIsNotNone(c.id)
            fetched = db.session.get(Category, c.id)
            self.assertEqual(fetched.type, "History")


if __name__ == "__main__":
    unittest.main()

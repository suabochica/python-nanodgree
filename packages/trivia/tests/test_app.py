import json
import unittest

from sqlalchemy.pool import StaticPool

from trivia import create_app
from trivia.models import Category, Question, db


# Plain-dict templates so each test gets fresh, unattached model
# instances (re-using module-level SQLAlchemy objects across sessions
# leaves them in a persistent state and the second `add_all` is a no-op).
CATEGORY_TEMPLATES = [
    {"type": "Science"},
    {"type": "Art"},
    {"type": "Geography"},
    {"type": "History"},
    {"type": "Entertainment"},
    {"type": "Sports"},
]


QUESTION_TEMPLATES = [
    {"id": 5, "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?", "answer": "Maya Angelou", "difficulty": 2, "category": 4},
    {"id": 9, "question": "What boxer's original name is Cassius Clay?", "answer": "Muhammad Ali", "difficulty": 1, "category": 4},
    {"id": 2, "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?", "answer": "Apollo 13", "difficulty": 4, "category": 5},
    {"id": 4, "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?", "answer": "Tom Cruise", "difficulty": 4, "category": 5},
    {"id": 6, "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?", "answer": "Edward Scissorhands", "difficulty": 3, "category": 5},
    {"id": 10, "question": "Which is the only team to play in every soccer World Cup tournament?", "answer": "Brazil", "difficulty": 3, "category": 6},
    {"id": 11, "question": "Which country won the first ever soccer World Cup in 1930?", "answer": "Uruguay", "difficulty": 4, "category": 6},
    {"id": 12, "question": "Who invented Peanut Butter?", "answer": "George Washington Carver", "difficulty": 2, "category": 4},
    {"id": 13, "question": "What is the largest lake in Africa?", "answer": "Lake Victoria", "difficulty": 2, "category": 3},
    {"id": 14, "question": "In which royal palace would you find the Hall of Mirrors?", "answer": "The Palace of Versailles", "difficulty": 3, "category": 3},
    {"id": 15, "question": "The Taj Mahal is located in which Indian city?", "answer": "Agra", "difficulty": 2, "category": 3},
    {"id": 16, "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?", "answer": "Escher", "difficulty": 1, "category": 2},
    {"id": 17, "question": "La Giaconda is better known as what?", "answer": "Mona Lisa", "difficulty": 3, "category": 2},
    {"id": 18, "question": "How many paintings did Van Gogh sell in his lifetime?", "answer": "One", "difficulty": 4, "category": 2},
    {"id": 19, "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?", "answer": "Jackson Pollock", "difficulty": 2, "category": 2},
    {"id": 20, "question": "What is the heaviest organ in the human body?", "answer": "The Liver", "difficulty": 4, "category": 1},
    {"id": 21, "question": "Who discovered penicillin?", "answer": "Alexander Fleming", "difficulty": 3, "category": 1},
    {"id": 22, "question": "Hematology is a branch of medicine involving the study of what?", "answer": "Blood", "difficulty": 4, "category": 1},
    {"id": 23, "question": "Which dung beetle was worshipped by the ancient Egyptians?", "answer": "Scarab", "difficulty": 4, "category": 4},
]


class TriviaTestCase(unittest.TestCase):
    """End-to-end tests for the Trivia API.

    Each test gets a fresh in-memory SQLite database via StaticPool so
    db.create_all() and subsequent queries share a single schema. The
    original tutorial tests used a separate `trivia_test` PostgreSQL
    database; the SQLite path is portable and doesn't require a running
    Postgres server.
    """

    TEST_CONFIG = {
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_ENGINE_OPTIONS": {
            "connect_args": {"check_same_thread": False},
            "poolclass": StaticPool,
        },
    }

    NEW_QUESTION = {
        "question": "What is the capital of France?",
        "answer": "Paris",
        "category": 3,
        "difficulty": 1,
    }

    SEARCH_TERM = {"searchTerm": "Tim Burton"}

    QUIZ_DATA = {
        "previous_questions": [3, 7],
        "quiz_category": {"type": "Entertainment", "id": 5},
    }

    def setUp(self):
        self.app = create_app(self.TEST_CONFIG)
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            db.session.add_all(Category(**data) for data in CATEGORY_TEMPLATES)
            db.session.add_all(Question(**data) for data in QUESTION_TEMPLATES)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
            db.engine.dispose()

    # ---- categories --------------------------------------------------------

    def test_get_categories(self):
        res = self.client.get("/categories")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertTrue(data["categories"])
        self.assertEqual(data["total_categories"], 6)

    def test_get_non_existent_category_returns_404(self):
        res = self.client.get("/categories/9999/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "Resource Not Found")

    # ---- questions ---------------------------------------------------------

    def test_get_questions_paginates_first_ten(self):
        res = self.client.get("/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertTrue(data["questions"])
        self.assertTrue(data["total_questions"])
        self.assertEqual(len(data["questions"]), 10)

    def test_get_non_existent_question_returns_404(self):
        res = self.client.get("/questions/9999")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "Resource Not Found")

    def test_get_questions_by_category(self):
        res = self.client.get("/categories/1/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertNotEqual(len(data["questions"]), 0)
        self.assertEqual(data["current_category"], "Science")

    def test_create_question_returns_201(self):
        res = self.client.post("/questions", json=self.NEW_QUESTION)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertTrue(data["success"])
        self.assertTrue(data["total_questions"])
        self.assertTrue(len(data["questions"]))

    def test_search_question(self):
        res = self.client.post("/questions", json=self.SEARCH_TERM)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertEqual(len(data["questions"]), 1)

    def test_delete_question(self):
        res = self.client.delete("/questions/23")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertEqual(data["deleted"], 23)
        self.assertTrue(data["questions"])
        self.assertTrue(data["total_questions"])

    # ---- quizzes -----------------------------------------------------------

    def test_play_quiz_excludes_previous_questions(self):
        res = self.client.post("/quizzes", json=self.QUIZ_DATA)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertTrue(data["question"])
        self.assertNotEqual(data["question"]["id"], 3)
        self.assertNotEqual(data["question"]["id"], 7)
        # NOTE: the model declares `category` as Column(String) even though
        # the PostgreSQL schema in trivia.psql uses integer. On SQLite this
        # round-trips as the string "5", so we assert against the string.
        self.assertEqual(data["question"]["category"], "5")


if __name__ == "__main__":
    unittest.main()

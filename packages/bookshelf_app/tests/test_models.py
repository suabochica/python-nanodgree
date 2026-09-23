import unittest
from sqlalchemy.pool import StaticPool

from bookshelf_app import create_app
from bookshelf_app.models import db, Book


class BookModelTestCase(unittest.TestCase):
    """Unit tests for the Book model that don't go through HTTP."""

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

    def test_format_returns_expected_shape(self):
        book = Book(title="Don Quixote", author="Cervantes", rating=10)
        self.assertEqual(
            book.format(),
            {
                "id": None,
                "title": "Don Quixote",
                "author": "Cervantes",
                "rating": 10,
            },
        )

    def test_insert_assigns_id_and_persists(self):
        with self.app.app_context():
            book = Book(title="Ulysses", author="Joyce", rating=9)
            book.insert()
            self.assertIsNotNone(book.id)
            fetched = db.session.get(Book, book.id)
            self.assertEqual(fetched.title, "Ulysses")
            self.assertEqual(fetched.rating, 9)

    def test_update_changes_rating(self):
        with self.app.app_context():
            book = Book(title="War and Peace", author="Tolstoy", rating=5)
            book.insert()
            book.rating = 10
            book.update()

            fetched = db.session.get(Book, book.id)
            self.assertEqual(fetched.rating, 10)

    def test_delete_removes_row(self):
        with self.app.app_context():
            book = Book(title="Beowulf", author="Anonymous", rating=7)
            book.insert()
            book_id = book.id
            book.delete()

            self.assertIsNone(db.session.get(Book, book_id))
            self.assertEqual(db.session.query(Book).count(), 0)


if __name__ == "__main__":
    unittest.main()

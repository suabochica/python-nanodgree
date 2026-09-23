import unittest
from sqlalchemy.pool import StaticPool

from bookshelf_app import create_app
from bookshelf_app.models import db


class BookshelfRoutesTestCase(unittest.TestCase):
    """End-to-end tests against the Flask test client.

    Each test gets a fresh app backed by an isolated in-memory SQLite
    database (StaticPool ensures the same connection is reused so
    db.create_all() and subsequent queries hit the same schema).
    """

    TEST_CONFIG = {
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_ENGINE_OPTIONS": {
            "connect_args": {"check_same_thread": False},
            "poolclass": StaticPool,
        },
    }

    def setUp(self):
        self.app = create_app(self.TEST_CONFIG)
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
            db.engine.dispose()

    def _post_book(self, title, author, rating):
        return self.client.post(
            "/books",
            json={"title": title, "author": author, "rating": rating},
        )

    def test_get_books_when_empty_returns_404(self):
        res = self.client.get("/books")
        self.assertEqual(res.status_code, 404)

    def test_post_books_creates_and_returns_payload(self):
        res = self._post_book("Don Quixote", "Miguel de Cervantes", 10)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data["success"])
        self.assertEqual(data["created"], 1)
        self.assertEqual(data["total_books"], 1)
        self.assertEqual(data["books"][0]["title"], "Don Quixote")

    def test_get_books_after_post_returns_paginated_list(self):
        for i in range(3):
            self._post_book(f"Title {i}", f"Author {i}", i + 5)

        res = self.client.get("/books")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["total_books"], 3)
        self.assertEqual(len(data["books"]), 3)

    def test_patch_book_updates_rating(self):
        self._post_book("Beowulf", "Anonymous", 7)
        res = self.client.patch("/books/1", json={"rating": 10})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), {"success": True, "id": 1})

        listed = self.client.get("/books").get_json()
        self.assertEqual(listed["books"][0]["rating"], 10)

    def test_delete_book_removes_it(self):
        self._post_book("Beowulf", "Anonymous", 7)
        res = self.client.delete("/books/1")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["deleted"], 1)
        self.assertEqual(data["total_books"], 0)

    def test_post_book_with_missing_fields_succeeds(self):
        # NOTE: the `books` schema allows NULLs and the route doesn't
        # validate, so posting a partial body still returns 200.
        res = self.client.post("/books", json={"title": "Incomplete"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["created"], 1)

    def test_patch_unknown_book_returns_400(self):
        # NOTE: the route wraps the handler in a bare `except:` that
        # catches the abort(404) and turns it into a 400.
        res = self.client.patch("/books/9999", json={"rating": 5})
        self.assertEqual(res.status_code, 400)

    def test_delete_unknown_book_returns_422(self):
        # Different bare `except:` clause on the DELETE route returns 422.
        res = self.client.delete("/books/9999")
        self.assertEqual(res.status_code, 422)

    def test_get_book_search_with_results(self):
        # Four books where "Novel" appears in either title or author,
        # plus one unrelated book that should not show up.
        for title, author, rating in [
            ("A Novel Beginning", "Author One", 8),
            ("Story of Love", "Novel Writer", 7),
            ("Mystery Novel", "Mystery Writer", 8),
            ("Another Book", "Joe Novel", 9),
            ("Cookbook", "Chef Person", 5),
        ]:
            self._post_book(title, author, rating)

        res = self.client.get("/books?search=Novel")
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertEqual(data["total_books"], 4)
        self.assertEqual(len(data["books"]), 4)

    def test_get_book_search_without_results(self):
        self._post_book("Don Quixote", "Cervantes", 10)

        res = self.client.get("/books?search=applejacks")
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertEqual(data["total_books"], 0)
        self.assertEqual(len(data["books"]), 0)


if __name__ == "__main__":
    unittest.main()

# bookshelf-app

Books CRUD REST API built with Flask, Flask-SQLAlchemy and Flask-CORS,
backed by PostgreSQL. The `template/` folder holds the React client that
consumes this API.

## Layout

```
bookshelf_app/
├── pyproject.toml
├── README.md
├── src/
│   └── bookshelf_app/
│       ├── __init__.py    # create_app() factory + main() entry point
│       └── models.py      # Book model and setup_db()
├── tests/                 # unittest TestCase suites
│   ├── __init__.py
│   ├── test_app.py        # HTTP route tests via Flask test_client
│   └── test_models.py     # Book model unit tests
└── template/              # React client (create-react-app)
```

## Prerequisites

- PostgreSQL running on `localhost:5432`
- `uv` for workspace management
- A `postgres` role with a known password (the app reads it from the
  `BOOKS_DB_PASSWORD` env var)
- Node.js 16+ and npm (for the React client)
  - On Node 17 or newer, the legacy OpenSSL provider must be enabled
    (see [Run the frontend](#run-the-frontend))

## Setup

```bash
# 1. Set a password for the postgres role (one-time)
sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD 'postgres';"

# 2. Create the bookshelf database
sudo -u postgres createdb bookshelfdb -O postgres

# 3. Install workspace deps
uv sync --package bookshelf-app
```

The `Book` table is created automatically on first run via `db.create_all()`
in `setup_db()`.

## Run the server

From the workspace root:

```bash
BOOKS_DB_PASSWORD=postgres uv run bookshelf-app
```

Expected startup output:

```
 * Serving Flask app 'bookshelf_app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.204:5000
Press CTRL+C to quit
```

## Endpoints

| Method   | Path                  | Description                |
| -------- | --------------------- | -------------------------- |
| `GET`    | `/books`              | List books (paginated, 8/page). Optional `?search=<term>` filters by title or author. |
| `POST`   | `/books`              | Create a new book          |
| `PATCH`  | `/books/<id>`         | Update a book's rating     |
| `DELETE` | `/books/<id>`         | Delete a book              |

### `GET /books`

```bash
curl -s http://127.0.0.1:5000/books | python3 -m json.tool
```

Expected output (empty database):

```
{}
```

Status: `200 OK` once at least one book exists, otherwise `404`.

### `GET /books?search=<term>`

Case-insensitive substring search against `title` **or** `author`. Always
returns `200` (an empty result set is a valid answer, distinct from "no
books at all" which 404s).

```bash
curl -s "http://127.0.0.1:5000/books?search=Novel" | python3 -m json.tool
```

Expected output (with matching books seeded):

```json
{
    "books": [
        {
            "author": "Author One",
            "id": 1,
            "rating": 8,
            "title": "A Novel Beginning"
        }
    ],
    "success": true,
    "total_books": 1
}
```

`total_books` is the count of **matches**, not the total in the DB.

## Seeding sample data

The `books` table is created automatically by `setup_db()` on first run.
To populate it with sample rows, POST a few books:

```bash
for book in \
  '{"title":"Don Quixote","author":"Miguel de Cervantes","rating":10}' \
  '{"title":"Ulysses","author":"James Joyce","rating":9}' \
  '{"title":"The Great Gatsby","author":"F. Scott Fitzgerald","rating":8}'; do
  curl -s -X POST http://127.0.0.1:5000/books \
    -H "Content-Type: application/json" \
    -d "$book" > /dev/null
done
```

Verify with `curl -s http://127.0.0.1:5000/books | python3 -m json.tool`.

### `POST /books`

```bash
curl -s -X POST http://127.0.0.1:5000/books \
  -H "Content-Type: application/json" \
  -d '{"title":"Don Quixote","author":"Miguel de Cervantes","rating":10}'
```

Expected output:

```json
{
    "books": [
        {
            "author": "Miguel de Cervantes",
            "id": 1,
            "rating": 10,
            "title": "Don Quixote"
        }
    ],
    "created": 1,
    "success": true,
    "total_books": 1
}
```

## Stopping the server

`Ctrl+C` in the terminal where `bookshelf-app` is running, or:

```bash
pkill -f bookshelf-app
```

## Run the frontend

The Flask backend only serves the JSON API — it does **not** host the
React UI. The UI lives in `template/` and runs as a separate process.

The app talks to the API through the `"proxy": "http://127.0.0.1:5000/"`
entry in `template/package.json`, so the Flask backend **must be running
on port 5000** before you start the React dev server.

```bash
# 1. Install the React deps (one-time)
cd packages/bookshelf_app/template
npm install
cd -

# 2. Start the dev server
cd packages/bookshelf_app/template
npm start
```

Then open **http://localhost:3000** in your browser.

> **Note for Node 17+:** `react-scripts@3.0.1` ships an old webpack that
> depends on OpenSSL algorithms removed from Node 17+. Without the
> legacy provider you'll see:
>
> ```
> Error: error:0308010C:digital envelope routines::unsupported
> ```
>
> Two ways to fix it:
>
> 1. Pass the flag inline:
>
>    ```bash
>    NODE_OPTIONS=--openssl-legacy-provider npm start
>    ```
>
> 2. Persist it via `template/.env` (create-react-app picks this up
>    automatically):
>
>    ```
>    NODE_OPTIONS=--openssl-legacy-provider
>    ```

### Port map

| Port | Process                | Serves                       |
| ---- | ---------------------- | ---------------------------- |
| 5000 | `bookshelf-app`        | JSON API (`/books`, `/books/<id>`) |
| 3000 | `react-scripts start`  | React UI                     |

### Stopping the frontend

`Ctrl+C` in the terminal where `npm start` is running, or:

```bash
pkill -f "react-scripts/scripts/start"
```

## Testing

Unit tests live in `tests/` (sibling of `src/`, **not** inside it) and
use only the standard library `unittest` package — no third-party test
runner required. They run `unittest.TestCase` subclasses, so `pytest`
will also discover and run them transparently.

Each test gets a fresh **in-memory SQLite** database via the
`test_config` argument of `create_app()`, so no PostgreSQL is needed to
run the suite.

```bash
# stdlib unittest (always available)
uv run python -m unittest discover -s packages/bookshelf_app/tests -v

# pytest (already in [dependency-groups] dev)
uv run pytest packages/bookshelf_app/tests -v
```

Expected output:

```
............
----------------------------------------------------------------------
Ran 12 tests in 0.10s

OK
```

### What's covered

- `tests/test_app.py` — HTTP routes through `Flask.test_client()`:
  empty list, POST create, GET list, PATCH rating, DELETE, plus the
  current behavior of error paths (some assertions document known app
  bugs and link them to the `bare except:` clauses in `src/bookshelf_app/__init__.py`).
- `tests/test_models.py` — `Book` model in isolation: `format()`,
  `insert()`, `update()`, `delete()` against an in-memory DB.

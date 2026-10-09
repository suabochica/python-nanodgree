# Trivia App

Udacity's trivia game: a Flask + SQLAlchemy + PostgreSQL API backing a
React client. Players pick a category and answer random questions, with
search and full CRUD over the question bank.

## Layout

```
trivia/
├── pyproject.toml
├── README.md
├── trivia.psql                  # seed data
├── src/
│   └── trivia/
│       ├── __init__.py          # create_app() factory + main() + all routes
│       └── models.py            # Question and Category
├── tests/                       # unittest TestCase suites
│   ├── __init__.py
│   ├── test_app.py              # HTTP route tests via Flask test_client
│   └── test_models.py           # Question / Category model unit tests
└── frontend/                    # React client (create-react-app)
```

## Prerequisites

- PostgreSQL running on `localhost:5432`
- `uv` for workspace management
- A `postgres` role with a known password
- Node.js 16+ and npm (for the React client — `package.json` already
  pins `NODE_OPTIONS=--openssl-legacy-provider` for Node 17+)

## Setup

```bash
# 1. Set a password for the postgres role (one-time)
sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD 'postgres';"

# 2. Create the trivia database
sudo -u postgres createdb trivia -O postgres

# 3. Seed the database
#    (the dump references the `student` role, so we rewrite to `postgres`)
sed 's/student/postgres/g' trivia.psql \
  | PGPASSWORD=postgres psql -U postgres -h localhost -d trivia

# 4. Install workspace deps
uv sync --package trivia
```

## Run the server

From the workspace root:

```bash
DATABASE_PASSWORD=postgres uv run trivia
```

The app reads DB credentials from these env vars (all optional except
`DATABASE_PASSWORD`):

| Variable           | Default        |
| ------------------ | -------------- |
| `DATABASE_NAME`    | `trivia`       |
| `DATABASE_USER`    | `postgres`     |
| `DATABASE_PASSWORD`| _(required)_   |
| `DATABASE_HOST`    | `localhost:5432` |

Expected startup output:

```
 * Serving Flask app 'trivia'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

The server listens on `http://0.0.0.0:5000` — same as the other apps in
this workspace, so stop the others first.

## Endpoints

| Method   | Path                                  | Description                            |
| -------- | ------------------------------------- | -------------------------------------- |
| `GET`    | `/categories`                         | List all categories                     |
| `GET`    | `/questions`                          | Paginated questions (10/page) + categories |
| `GET`    | `/questions/<id>`                     | Fetch a single question                 |
| `POST`   | `/questions`                          | Create a question **or** search (`{"searchTerm": "..."}`) |
| `DELETE` | `/questions/<id>`                     | Delete a question                       |
| `GET`    | `/categories/<id>/questions`          | Questions filtered by category          |
| `POST`   | `/quizzes`                            | Random question, excluding previous     |

All errors are returned as JSON:

```json
{"success": false, "error": 404, "message": "Resource Not Found"}
```

## Run the frontend

The Flask backend only serves the JSON API — the React UI lives in
`frontend/` and runs on a separate process. It talks to the API through
`"proxy": "http://127.0.0.1:5000/"` in `frontend/package.json`, so the
Flask backend **must be running on port 5000** before you start the
React dev server.

```bash
cd packages/trivia/frontend
npm install
npm start
```

Then open **http://localhost:3000** in your browser.

> The `package.json` already sets
> `NODE_OPTIONS=--openssl-legacy-provider` for `start` and `build`, so
> no extra env work is needed for Node 17+.

### Port map

| Port | Process       | Serves                          |
| ---- | ------------- | ------------------------------- |
| 5000 | `trivia`      | JSON API                        |
| 3000 | `react-scripts start` | React UI                 |

## Testing

Unit tests live in `tests/` and use only the standard library `unittest`
package. Each test gets a fresh in-memory SQLite database via the
`test_config` argument of `create_app()`, so no PostgreSQL is needed to
run the suite.

```bash
# stdlib unittest (always available)
uv run python -m unittest discover -s packages/trivia/tests -v

# pytest (already in [dependency-groups] dev)
uv run pytest packages/trivia/tests -v
```

Expected output:

```
...............
----------------------------------------------------------------------
Ran 15 tests in 0.13s

OK
```

### What's covered

- `tests/test_app.py` — 9 HTTP route tests through `Flask.test_client()`:
  categories, questions list, paginated questions, create, search,
  delete, single-question fetch, by-category, and the quiz endpoint
  excluding previous questions.
- `tests/test_models.py` — 6 `Question` and `Category` model unit
  tests: `format()`, insert / update / delete persistence.

## Stopping the server

`Ctrl+C` in the terminal where `trivia` is running, or:

```bash
pkill -f "trivia$"          # the entry point
pkill -f "react-scripts/scripts/start"   # the frontend
```

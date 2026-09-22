# plants-app

Dummy plants REST API built with Flask, Flask-SQLAlchemy and Flask-CORS,
backed by PostgreSQL. Part of the Udacity Full-Stack Nanodegree practice
apps.

## Prerequisites

- PostgreSQL running on `localhost:5432`
- `uv` for workspace management
- A `postgres` role with a known password (the app reads it from the
  `PLANTS_DB_PASSWORD` env var)

## Setup

```bash
# 1. Set a password for the postgres role (one-time)
sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD 'postgres';"

# 2. Create the plantsdb database
sudo -u postgres createdb plantsdb -O postgres

# 3. Seed the plants table (the dump references the `student` role, so we
#    rewrite it to `postgres` on the fly)
sed 's/student/postgres/g' packages/plants_app/plants.psql \
  | PGPASSWORD=postgres psql -U postgres -h localhost -d plantsdb

# 4. Install workspace deps
uv sync --package plants-app
```

## Run the server

From the workspace root:

```bash
PLANTS_DB_PASSWORD=postgres uv run plants-app
```

Expected startup output:

```
 * Serving Flask app 'plants_app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.204:5000
Press CTRL+C to quit
```

The app listens on `http://0.0.0.0:5000`.

## Endpoints

### `GET /plants`

Returns a paginated list of plants (10 per page).

```bash
curl -s http://127.0.0.1:5000/plants | python3 -m json.tool
```

Expected output (truncated):

```json
{
    "plants": [
        {
            "id": 1,
            "is_poisonous": true,
            "name": "Hydrangea",
            "primary_color": "blue",
            "scientific_name": "Hydrangea macrophylla"
        },
        {
            "id": 2,
            "is_poisonous": true,
            "name": "Oleander",
            "primary_color": "pinik",
            "scientific_name": "Nerium oleander"
        },
        ...
    ]
}
```

Status: `200 OK`.

### `GET /plants/<id>`

Returns a single plant by id, or 404 if not found.

```bash
curl -s -w "\nHTTP %{http_code}\n" http://127.0.0.1:5000/plants/3
```

Expected output:

```
{"plant":{"id":3,"is_poisonous":true,"name":"Water Hemlock","primary_color":"white","scientific_name":"Cicuta"},"success":true}

HTTP 200
```

For a missing id:

```bash
curl -s -w "\nHTTP %{http_code}\n" http://127.0.0.1:5000/plants/9999
```

```
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>

HTTP 404
```

## Stopping the server

`Ctrl+C` in the terminal where `plants-app` is running, or:

```bash
pkill -f plants-app
```

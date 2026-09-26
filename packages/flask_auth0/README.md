# flask-auth0

Demo Flask API that validates Auth0 RS256 JWT bearer tokens on a single
`/headers` route. Returns the decoded JWT payload when the token is valid.

## Layout

```
flask_auth0/
├── pyproject.toml
├── README.md
└── src/
    └── flask_auth0/
        └── __init__.py    # AuthError, token helpers, requires_auth,
                           # create_app() factory + main() entry point
```

## Prerequisites

- Python 3.14+ (matches the workspace constraint)
- An Auth0 account (free tier is fine) — see
  [Setting up Auth0](#setting-up-auth0) below
- `uv` for workspace management

## Setup

```bash
# 1. Install workspace deps
uv sync --package flask-auth0
```

## Configuration

The app reads its Auth0 credentials from environment variables — **do not
hardcode them** in `__init__.py`:

| Variable        | Example value                  | Notes                  |
| --------------- | ------------------------------ | ---------------------- |
| `AUTH0_DOMAIN`  | `dev-abc123.us.auth0.com`      | Your tenant domain     |
| `API_AUDIENCE`  | `https://my-api.example.com`   | The API identifier     |

If either variable is missing, the app falls back to the placeholder
strings `TODO_REPLACE_WITH_YOUR_DOMAIN` and
`TODO_REPLACE_WITH_YOUR_API_AUDIENCE`, and token verification will fail
with an `invalid_header` error.

```bash
export AUTH0_DOMAIN=dev-abc123.us.auth0.com
export API_AUDIENCE=https://my-api.example.com
```

## Run the server

```bash
AUTH0_DOMAIN=dev-abc123.us.auth0.com \
  API_AUDIENCE=https://my-api.example.com \
  uv run flask-auth0
```

Expected startup output:

```
 * Serving Flask app 'flask_auth0'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.204:5000
Press CTRL+C to quit
```

The server listens on `http://0.0.0.0:5000` — same as `plants-app` and
`bookshelf-app`, so stop one before running another.

## Endpoint

### `GET /headers` (requires Bearer token)

Decodes the JWT and returns its payload. Without a valid
`Authorization: Bearer <token>` header it returns `401`.

```bash
curl -s -H "Authorization: Bearer $TOKEN" \
  http://127.0.0.1:5000/headers | python3 -m json.tool
```

Expected output (shape, contents vary by Auth0 config):

```json
{
    "payload": {
        "iss": "https://dev-abc123.us.auth0.com/",
        "sub": "auth0|000000000000000000000000",
        "aud": "https://my-api.example.com",
        "iat": 1700000000,
        "exp": 1700003600
    },
    "success": true
}
```

Without a token (or with an invalid one), the response is `401`.

## Setting up Auth0

1. Create a free Auth0 account at <https://auth0.com>.
2. Pick a unique tenant domain (used as `AUTH0_DOMAIN`).
3. Create a new **API** in the Auth0 dashboard — its identifier becomes
   `API_AUDIENCE`.
4. From a front-end / Postman, get a valid access token by logging in.
   Send it as `Authorization: Bearer <token>` to `/headers`.

## Stopping the server

`Ctrl+C` in the terminal where `flask-auth0` is running, or:

```bash
pkill -f flask-auth0
```

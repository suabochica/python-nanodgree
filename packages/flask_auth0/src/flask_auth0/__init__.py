import json
import os
from functools import wraps
from urllib.request import urlopen

from flask import Flask, abort, jsonify, request
from flask_cors import CORS
from jose import jwt


__version__ = "0.1.0"

# ---------------------------------------------------------------------------
# Auth0 configuration
# ---------------------------------------------------------------------------
# Set these via environment variables before running the server. The
# placeholder defaults make the app refuse to start (rather than auth
# silently with bogus values).
AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN", "TODO_REPLACE_WITH_YOUR_DOMAIN")
API_AUDIENCE = os.environ.get("API_AUDIENCE", "TODO_REPLACE_WITH_YOUR_API_AUDIENCE")
ALGORITHMS = ["RS256"]


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


# ---------------------------------------------------------------------------
# Token helpers
# ---------------------------------------------------------------------------
def get_token_auth_header():
    """Obtains the Access Token from the Authorization Header."""
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError(
            {
                "code": "authorization_header_missing",
                "description": "Authorization header is expected.",
            },
            401,
        )

    parts = auth.split()
    if parts[0].lower() != "bearer":
        raise AuthError(
            {
                "code": "invalid_header",
                "description": 'Authorization header must start with "Bearer".',
            },
            401,
        )
    elif len(parts) == 1:
        raise AuthError(
            {"code": "invalid_header", "description": "Token not found."}, 401
        )
    elif len(parts) > 2:
        raise AuthError(
            {
                "code": "invalid_header",
                "description": "Authorization header must be bearer token.",
            },
            401,
        )

    return parts[1]


def verify_decode_jwt(token):
    jsonurl = urlopen(f"https://{AUTH0_DOMAIN}/.well-known/jwks.json")
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}

    if "kid" not in unverified_header:
        raise AuthError(
            {
                "code": "invalid_header",
                "description": "Authorization malformed.",
            },
            401,
        )

    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"],
            }

    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer="https://" + AUTH0_DOMAIN + "/",
            )
            return payload
        except jwt.ExpiredSignatureError:
            raise AuthError(
                {"code": "token_expired", "description": "Token expired."}, 401
            )
        except jwt.JWTClaimsError:
            raise AuthError(
                {
                    "code": "invalid_claims",
                    "description": "Incorrect claims. Please, check the audience and issuer.",
                },
                401,
            )
        except Exception:
            raise AuthError(
                {
                    "code": "invalid_header",
                    "description": "Unable to parse authentication token.",
                },
                400,
            )

    raise AuthError(
        {
            "code": "invalid_header",
            "description": "Unable to find the appropriate key.",
        },
        400,
    )


def requires_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = get_token_auth_header()
        try:
            payload = verify_decode_jwt(token)
        except AuthError:
            abort(401)
        return f(payload, *args, **kwargs)

    return wrapper


def check_permissions(permission, payload):
    if "permissions" not in payload:
        raise AuthError(
            {
                "code": "invalid_claims",
                "description": "Permissions not included in JWT.",
            },
            400,
        )

    if permission not in payload["permissions"]:
        raise AuthError(
            {"code": "unauthorized", "description": "Permission not found."}, 403
        )
    return True


# ---------------------------------------------------------------------------
# App factory
# ---------------------------------------------------------------------------
def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add("Access-Control-Allow-Methods", "GET,POST,DELETE,OPTIONS")
        return response

    @app.route("/headers")
    @requires_auth
    def headers(payload):
        return jsonify({"success": True, "payload": payload})

    return app


def main():
    app = create_app()
    app.run(host="0.0.0.0", port=5000)

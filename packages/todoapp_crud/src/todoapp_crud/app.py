from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import sys

load_dotenv(Path(__file__).resolve().parents[4] / ".env")

app = Flask(__name__)

import os

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<Todo {self.id} | {self.description}>"


@app.route("/todos/create", methods=["POST"])
def create_todo():
    error = False
    body = []

    try:
        description = request.json.get("description")
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
        body["description"] = todo.description
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.sesison.close()
    if error:
        abord(400)
    else:
        return jsonify(body)


@app.route("/")
def index():
    return render_template(
        "index.html",
        data=Todo.query.all(),
    )


# always include this at the bottom of your code
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

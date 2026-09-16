from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

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


@app.route("/")
def index():
    return render_template(
        "index.html",
        data=Todo.query.all(),
    )


# always include this at the bottom of your code
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

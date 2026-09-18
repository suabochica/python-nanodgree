from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify, abort, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys
import os

load_dotenv(Path(__file__).resolve().parents[4] / ".env")

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class TodoList(db.Model):
    __tablename__ = "todolists"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    todos = db.relationship("Todo", backref="list", lazy=True)

    def __repr__(self):
        return f"<TodoList {self.id} {self.name}>"


class Todo(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    list_id = db.Column(db.Integer, db.ForeignKey("todolists.id"), nullable=True)

    def __repr__(self):
        return f"<Todo {self.id} {self.description}, list {self.list_id}>"


@app.route("/todos/create", methods=["POST"])
def create_todo():
    error = False
    body = {}
    try:
        description = request.get_json()["description"]
        list_id = request.get_json()["list_id"]
        todo = Todo(description=description)
        active_list = db.session.get(TodoList, list_id)
        todo.list = active_list
        db.session.add(todo)
        db.session.commit()
        body["id"] = todo.id
        body["description"] = todo.description
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if not error:
        return jsonify(body)
    else:
        abort(500)


@app.route("/todos/<todo_id>/set-completed", methods=["POST"])
def set_completed_todo(todo_id):
    try:
        completed = request.get_json()["completed"]

        todo = db.session.get(Todo, todo_id)
        todo.completed = completed
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()

    return redirect(url_for("index"))


@app.route("/todos/<todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    try:
        Todo.query.filter_by(id=todo_id).delete()
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()

    return jsonify({"success": True})


@app.route("/lists/<list_id>")
def get_list_todos(list_id):
    return render_template(
        "index.html",
        lists=TodoList.query.all(),
        active_list=db.session.get(TodoList, list_id),
        todos=Todo.query.filter_by(list_id=list_id).order_by(Todo.id),
    )


@app.route("/lists/create", methods=["POST"])
def create_list():
    error = False
    body = {}
    try:
        name = request.get_json()["name"]
        todolist = TodoList(name=name)
        db.session.add(todolist)
        db.session.commit()
        body["id"] = todolist.id
        body["name"] = todolist.name
    except ():
        db.session.rollback()
        error = True
        print(sys.exc_info)
    finally:
        db.session.close()
    if error:
        abort(500)
    else:
        return jsonify(body)


@app.route("/lists/<list_id>/delete", methods=["DELETE"])
def delete_list(list_id):
    error = False
    try:
        list = TodoList.query.get(list_id)
        for todo in list.todos:
            db.session.delete(todo)

        db.session.delete(list)
        db.session.commit()
    except ():
        db.session.rollback()
        error = True
    finally:
        db.session.close()
    if error:
        abort(500)
    else:
        return jsonify({"success": True})


@app.route("/lists/<list_id>/set-completed", methods=["POST"])
def set_completed_list(list_id):
    error = False
    try:
        list = TodoList.query.get(list_id)
        for todo in list.todos:
            todo.completed = True
        db.session.commit()
    except:
        db.session.rollback()
        error = True
    finally:
        db.session.close()
    if error:
        abort(500)
    else:
        return "", 200


@app.route("/")
def index():
    return redirect(url_for("get_list_todos", list_id=1))


# always include this at the bottom of your code
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debut=true)

import random

from flask import Blueprint, Flask, abort, jsonify, request
from flask_cors import CORS

from .models import Category, Question, db, setup_db


__version__ = "0.1.0"

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    return questions[start:end]


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        setup_db(app)
    else:
        database_path = test_config.get("SQLALCHEMY_DATABASE_URI")
        setup_db(app, database_path=database_path)

    CORS(app, resources={"/": {"origins": "*"}})
    with app.app_context():
        db.create_all()

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Authorization"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET, POST, PATCH, DELETE, OPTIONS"
        )
        return response

    api = Blueprint("api", __name__, url_prefix="/api")

    @api.route("/categories")
    def get_categories():
        categories = Category.query.all()

        try:
            return jsonify(
                {
                    "success": True,
                    "categories": {
                        category.id: category.type for category in categories
                    },
                    "total_categories": len(categories),
                }
            )
        except:
            abort(404)

    @api.route("/questions")
    def get_questions():
        questions = Question.query.order_by(Question.id).all()
        categories = Category.query.order_by(Category.id).all()

        if len(categories) == 0:
            abort(404)

        current_questions = paginate_questions(request, selection=questions)

        return jsonify(
            {
                "success": True,
                "questions": current_questions,
                "total_questions": len(questions),
                "categories": {
                    category.id: category.type for category in categories
                },
                "current_category": categories[0].type,
            }
        )

    @api.route("/questions/<int:question_id>", methods=["GET", "DELETE"])
    def question_detail(question_id):
        question = Question.query.filter(Question.id == question_id).one_or_none()

        if question is None:
            abort(404)

        if request.method == "DELETE":
            question.delete()
            questions = Question.query.order_by(Question.id).all()
            current_question = paginate_questions(request, selection=questions)

            return jsonify(
                {
                    "success": True,
                    "deleted": question_id,
                    "questions": current_question,
                    "total_questions": len(questions),
                },
            )

        return jsonify({"success": True, "question": question.format()})

    @api.route("/questions", methods=["POST"])
    def create_question():
        body = request.get_json()

        new_question = body.get("question", "")
        new_answer = body.get("answer", "")
        new_category = body.get("category", 1)
        new_difficulty = body.get("difficulty", 1)
        search_term = body.get("searchTerm", "")

        if (new_question == "" or new_answer == "") and search_term == "":
            abort(422)

        try:
            if search_term:
                search_result = Question.query.filter(
                    Question.question.ilike(f"%{search_term}%")
                ).all()
                current_result = paginate_questions(request, selection=search_result)

                return jsonify(
                    {
                        "success": True,
                        "questions": current_result,
                        "total_questions": len(search_result),
                    }
                )
            else:
                question = Question(
                    question=new_question,
                    answer=new_answer,
                    category=new_category,
                    difficulty=new_difficulty,
                )
                question.insert()
                questions = Question.query.order_by(Question.id).all()
                current_questions = paginate_questions(request, selection=questions)

                return (
                    jsonify(
                        {
                            "success": True,
                            "created": question.id,
                            "questions": current_questions,
                            "total_questions": len(questions),
                        }
                    ),
                    201,
                )

        except:
            abort(422)

    @api.route("/categories/<int:category_id>/questions")
    def get_questions_by_category(category_id):
        try:
            category = Category.query.filter(Category.id == category_id).one_or_none()

            if category is None:
                abort(404)

            questions = (
                Question.query.order_by(Question.id)
                .filter(Question.category == category_id)
                .all()
            )
            current_question = paginate_questions(request, selection=questions)

            return jsonify(
                {
                    "success": True,
                    "questions": current_question,
                    "total_questions": len(questions),
                    "current_category": category.type,
                }
            )
        except:
            abort(404)

    @api.route("/quizzes", methods=["POST"])
    def play_quiz():
        body = request.get_json()
        previous_questions = body.get("previous_questions", [])
        quiz_category = body.get("quiz_category", None)

        try:
            if quiz_category and quiz_category.get("id"):
                questions = Question.query.filter(
                    Question.category == quiz_category["id"]
                ).all()
            else:
                questions = Question.query.all()

            remaining = [q for q in questions if q.id not in previous_questions]

            if not remaining:
                return jsonify({"success": True, "question": None})

            question = random.choice(remaining)
            return jsonify({"success": True, "question": question.format()})
        except:
            abort(422)

    @app.errorhandler(400)
    def bad_request(error):
        return (
            jsonify({"success": False, "error": 400, "message": "Bad Request"}),
            400,
        )

    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify(
                {"success": False, "error": 404, "message": "Resource Not Found"}
            ),
            404,
        )

    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify({"success": False, "error": 422, "message": "Unprocessable"}),
            422,
        )

    @app.errorhandler(500)
    def internal_server_error(error):
        return (
            jsonify(
                {
                    "success": False,
                    "error": 500,
                    "message": "Internal Server Error",
                }
            ),
            500,
        )

    app.register_blueprint(api)

    return app


def main():
    app = create_app()
    app.run(host="0.0.0.0", port=5000)

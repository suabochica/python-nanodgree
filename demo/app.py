from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://suabochica:Alkahestri4!@localhost:5432/suabochica"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__: "persons"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Person ID: {self.id}, name: {self.name}>"


with app.app_context():
    db.create_all()
    if not Person.query.first():
        db.session.add(Person(name="Alice"))
        db.session.commit()


@app.route("/")
def index():
    person = Person.query.first()
    if not person:
        return "Hello, World!"
    return "Hello " + person.name

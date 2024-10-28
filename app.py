from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route("/")
def hello_world():
    todo = Todo(title="Demo task 1", desc="Invest in my relationships with people")
    db.session.add(todo)
    db.session.commit()
    allTodos = Todo.query.all()
    print(allTodos)
    return render_template("index.html", allTodos=allTodos)


@app.route("/products")
def product():
    return "this is the page for product page!"


@app.route("/shows")
def showAll():
    allTodos = Todo.query.all()
    print(allTodos)
    return "printed all todos"


def create_tables():
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    create_tables()
    app.run(debug=True, port=8000)

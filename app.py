
from flask import Flask, redirect, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Swarda31%40@localhost/todo_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


@app.route("/", methods=['GET', 'POST'])
def hello_world():

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        todo = Todo(title=title, description=description)
        db.session.add(todo)
        db.session.commit()

    allTodo = Todo.query.all()

    return render_template("index.html", allTodo=allTodo)


@app.route("/show")
def show():
    allTodo = Todo.query.all()
    print(allTodo)
    return "This is the show page of the todo application"

@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):

    todo = Todo.query.filter_by(id=id).first()

    if request.method == 'POST':
        todo.title = request.form['title']
        todo.description = request.form['description']

        db.session.commit()
        return redirect("/")

    return render_template("update.html", todo=todo)
@app.route("/delete/<int:id>")
def delete(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
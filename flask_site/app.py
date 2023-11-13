from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

project_directory = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_directory, "mydatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)


class Book(db.Model):
    name = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)
    author = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/addbook")
def addbook():
    return render_template("addbook.html")


@app.route("/updatebook")
def updatebook():
    books = Book.query.all()
    return render_template("updatebook.html", books=books)


@app.route("/update", methods=["POST"])
def update():
    old_book_name = request.form["old_bookname"]
    new_book_name = request.form["new_bookname"]
    new_author_name = request.form["new_authorname"]

    book = Book.query.filter_by(name=old_book_name).first()
    book.name = new_book_name
    book.author = new_author_name
    db.session.commit()
    return redirect("/books")


@app.route("/delete", methods=["POST"])
def delete():
    name = request.form["name"]

    book = Book.query.filter_by(name=name).first()
    book.name = name
    db.session.delete(book)
    db.session.commit()
    return redirect("/books")


@app.route("/supdate", methods=["POST"])
def submitbook():
    book_name = request.form["book_name"]
    author_name = request.form["author_name"]
    book = Book(name=book_name, author=author_name)
    db.session.add(book)
    db.session.commit()
    return redirect("/books")


@app.route("/books")
def books():
    books = Book.query.all()
    return render_template("books.html", books=books)


@app.route("/profile/<username>")
def profile(username):
    return render_template("profile.html", username=username, isActive=False)


@app.route("/admin")
def welcome_admin():
    return "<h1>WELCOME ADMIN</h1>"


@app.route("/guest/<guest>")
def welcome_guest(guest):
    return "<h1>WELCOME GUEST %s</h1>" % guest.upper()


@app.route("/user/<username>")
def welcome_user(username):
    if username == "admin":
        return redirect(url_for("welcome_admin"))
    else:
        return redirect(url_for("welcome_guest", guest=username))


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "mydatabase.db"))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50), nullable=False)
    expensename = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False)


@app.route("/")
def add():
    return render_template("add.html")


@app.route("/expenses")
def expenses():
    expenses = Expense.query.all()
    total = 0
    t_food = 0
    t_entertainment = 0
    t_business = 0
    t_other = 0

    for expense in expenses:
        total += expense.amount
        if expense.category == "food":
            t_food += expense.amount
        elif expense.category == "business":
            t_business += expense.amount
        elif expense.category == "other":
            t_other += expense.amount
        elif expense.category == "entertainment":
            t_entertainment += expense.amount

        print(total)

    return render_template(
        "expenses.html",
        expenses=expenses,
        total=total,
        t_food=t_food,
        t_business=t_business,
        t_entertainment=t_entertainment,
        t_other=t_other,
    )


@app.route("/delete/<int:id>")
def delete(id):
    expenses = Expense.query.filter_by(id=id).first()
    db.session.delete(expenses)
    db.session.commit()

    return redirect("/expenses")


@app.route("/edit/<int:id>")
def edit(id):
    expense = Expense.query.filter_by(id=id).first()

    return render_template("edit.html", expense=expense)


@app.route("/update", methods=["POST"])
def update():
    id = request.form["id"]
    date = request.form["date"]
    amount = request.form["amount"]
    expensename = request.form["expensename"]
    category = request.form["category"]
    expense = Expense.query.filter_by(id=id).first()
    expense.date = date
    expense.amount = amount
    expense.category = category
    expense.expensename = expensename
    db.session.commit()

    return redirect("/expenses")


@app.route("/addexpense", methods=["POST"])
def addexpense():
    date = request.form["date"]
    amount = request.form["amount"]
    expensename = request.form["expensename"]
    category = request.form["category"]

    expenses = Expense(
        date=date, amount=amount, category=category, expensename=expensename
    )
    db.session.add(expenses)
    db.session.commit()
    return redirect("/expenses")


@app.route("/appview")
def appview():
    if request.method == "GET":
        expenses = Expense.query.all()
        total = 0
        t_food = 0
        t_entertainment = 0
        t_business = 0
        t_other = 0

        for expense in expenses:
            total += expense.amount
            if expense.category == "food":
                t_food += expense.amount
            elif expense.category == "business":
                t_business += expense.amount
            elif expense.category == "other":
                t_other += expense.amount
            elif expense.category == "entertainment":
                t_entertainment += expense.amount

            print(total)
    elif request.method == "GET":
        date = request.form["date"]
        amount = request.form["amount"]
        expensename = request.form["expensename"]
        category = request.form["category"]

        expenses = Expense(
            date=date, amount=amount, category=category, expensename=expensename
        )
        db.session.add(expenses)
        db.session.commit()
        return redirect("/appview")

    return render_template(
        "expenses.html",
        expenses=expenses,
        total=total,
        t_food=t_food,
        t_business=t_business,
        t_entertainment=t_entertainment,
        t_other=t_other,
    )


if __name__ == "__main__":
    app.run(debug=True)

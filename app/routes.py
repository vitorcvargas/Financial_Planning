from flask import render_template, request, redirect, url_for
from app import app
from .functions import *
from .models import *


@app.route("/")
def index():

    # shows current balance
    current_balance = Balance.query.first().balance

    daily_limit = limit(current_balance)    

    return render_template('index.html', current_balance = "$ {}".format(round(current_balance, 2)), daily_limit = "$ {}".format(round(daily_limit, 2)))

@app.route("/add", methods = ["POST"])
def add():

    income_amount = int(request.form.get('income_amount'))
    income_source = request.form.get('income_source')

    expense_amount = int(request.form.get('expense_amount'))
    expense_source = request.form.get('expense_source')

    income = Income(amount = income_amount, source = income_source)
    expense = Expense(amount = expense_amount, source = expense_source)
    balance = Balance(balance = income_amount - expense_amount)

    db.session.add(income)
    db.session.add(expense)
    db.session.add(balance)

    db.session.commit()

    return redirect(url_for('index'))

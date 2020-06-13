from flask import render_template, request, redirect, url_for
from app import app
from .functions import *
from .models import *


@app.route("/")
def index():
    
    balance = Balance.query.first()

    if balance != None:
        
        current_balance = balance.balance
        daily_limit = limit(current_balance)

        return render_template('index.html', balance = balance, 
        current_balance = "{:.2f}".format(current_balance), 
        daily_limit = "{:.2f}".format(daily_limit))

    else:
        return render_template('index.html', balance = balance)

@app.route("/update/<int:id>", methods = ["POST"])
def update(id):

    item = Balance.query.get(id)
    update = request.form.get('current_balance')
    item.balance = update
    db.session.commit()

    return redirect(url_for('index'))        


@app.route("/create", methods = ["POST"])
def create():
    
    item = Balance(balance = request.form.get('current_balance'))
    
    db.session.add(item)
    db.session.commit()

    return redirect(url_for('index'))        



@app.route("/income", methods = ["POST"])
def income():

    income_amount = int(request.form.get('income_amount'))
    income_source = request.form.get('income_source')

    balance = Balance.query.first()

    balance.income(income_amount)
    income = Income(amount = income_amount, source = income_source)
    
    db.session.add(income)
    db.session.commit()

    return redirect(url_for('index'))

@app.route("/expense", methods = ["POST"])
def expense():

    expense_amount = int(request.form.get('expense_amount'))
    expense_source = request.form.get('expense_source')

    balance = Balance.query.first()

    balance.expense(expense_amount)
    expense = Expense(amount = expense_amount, source = expense_source)

    db.session.add(expense)    
    db.session.commit()

    return redirect(url_for('index'))

from app import db


class Balance(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    balance = db.Column(db.Float(asdecimal = True), default = 0)
    incomes = db.relationship('Income', lazy = True)
    expenses = db.relationship('Expense', lazy = True)

    def __repr__(self):
        return f"Balance('{self.balance}')"

class Income(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    amount = db.Column(db.Float(asdecimal = True), default = 0)
    source = db.Column(db.String(50))
    balance_id = db.Column(db.Integer, db.ForeignKey('balance.id'))

    def __repr__(self):
        return f"Income('{self.source}')"

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    amount = db.Column(db.Float(asdecimal = True), default = 0)
    source = db.Column(db.String(50))
    balance_id = db.Column(db.Integer, db.ForeignKey('balance.id'))

    def __repr__(self):
        return f"Income('{self.source}')"



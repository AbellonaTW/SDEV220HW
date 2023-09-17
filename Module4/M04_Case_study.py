from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

#route says when you go to this url.. perform the following fucntion
@app.route('/')
def index():
    return 'Hello!'

#model - python-y version of a db table. Through classes
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120))
    publisher = db.Column(db.String(160))

    def __repr__(self):
        return f"{self.book_name} is a book written by {self.author}, and was published by {self.publisher}"
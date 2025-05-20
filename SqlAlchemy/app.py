from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'book_db.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    author = db.Column(db.String(40), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __str__(self):
        return f''' 
        book title - {self.title}
        author - {self.author}
        price - {self.price}
        '''

import os

with app.app_context():
    print("DB path:", os.path.abspath('book_db.sqlite'))

with app.app_context():
    db.create_all()

    b1 = Books.query.first()
    all_books = Books.query.all()
    all_books_by_author = Books.query.filter_by(author='William Shakespeare').all()
    for book in all_books_by_author:
        print(book)

    db.session.add(Books(title="test", author="test", price=14))
    db.session.commit()
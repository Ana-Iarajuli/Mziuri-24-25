import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'book_db.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(35), nullable=False)
    author = db.Column(db.String(40), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"title: {self.title}\nauthor: {self.author}\nprice: {self.price}"


with app.app_context():
    book1 = Books.query.first()
    all_books = Books.query.all()
    rowling_books = Books.query.filter_by(author="Rowling").all()
    for book in rowling_books:
        print(book)
    print(book1)

    # ADD A BOOK FUNCTIONALITY
    title = "ზებულონი"
    author = "ქარჩხაძე"
    price = 19.5
    new_book = Books(title=title, author=author, price=price)

    db.session.add(new_book)
    db.session.commit()
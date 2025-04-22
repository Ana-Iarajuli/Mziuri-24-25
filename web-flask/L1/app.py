from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Home Page</h1>"


@app.route('/about')
def about():
    return '<p>This is about us page</p>'


if __name__ == "__main__":
    app.run(debug=True)

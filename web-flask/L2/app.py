from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Home Page</h1>"


@app.route('/about')
def about():
    return '<p>This is about us page</p>'


@app.route('/<name>/<surname>/<int:age>/')
def profile(name, surname, age):
    subjects = ["ქართული", "მათემატიკა", "ინგლისური"]
    return render_template("user.html",
                           user_name=name,
                           user_surname=surname,
                           user_age=age,
                           user_subjects=subjects)


@app.route('/admin')
def admin():
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)





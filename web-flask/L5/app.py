from flask import (Flask, render_template, request,
                   redirect, url_for, session)
app = Flask(__name__)

#bonus question - funqcia da method - lazare

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/profile")
def profile():
    username = session["user"]
    password = session["password"]
    return render_template("profile.html", username=username,
                           password=password)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        user_password = request.form["password"]
        session["user"] = username
        session["password"] = user_password
        return redirect(url_for("profile"))
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
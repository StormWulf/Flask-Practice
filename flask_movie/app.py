from flask import (
    Flask,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_sqlalchemy import SQLAlchemy
from passwords import POSTGRES_PASSWORD

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{POSTGRES_PASSWORD}@localhost/flask_movie'
app.debug = True
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return f"<User {self.username}>"


@app.route("/")
def index():
    users = User.query.all()
    one_item = User.query.filter_by(username="foo").first()
    return render_template("add_user.html", users=users, one_item=one_item)


@app.route("/profile/<username>")
def profile(username):
    user = User.query.filter_by(username=username).first()
    return render_template("profile.html", user=user)


@app.route("/post_user", methods=["POST"])
def post_user():
    user = User(request.form['username'], request.form['email'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()

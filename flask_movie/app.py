from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from passwords import POSTGRES_PASSWORD

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{POSTGRES_PASSWORD}@localhost/flask_movie'
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
    return "<h1 style='color: red'>Hello Flask</h1>"


if __name__ == "__main__":
    app.run()

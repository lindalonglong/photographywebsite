from flask import Flask

from flask import Flask, render_template,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField
from wtforms.validators import InputRequired,Email,Length
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


import projects


app = Flask(__name__)


@app.route('/')
def home_route():
    return render_template("home.html", projects=projects.setup())

@app.route('/photos/')
def hello_route():
    return render_template("photos.html", projects=projects.setup())


if __name__ == "__main__":
    app.run(debug = True, port=8080)
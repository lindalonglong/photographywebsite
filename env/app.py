from flask import Flask

from flask import Flask, render_template,redirect,url_for
from env import projects



app = Flask(__name__)


@app.route('/')
def home_route():
    return render_template("home.html", projects=projects.setup())

@app.route('/photos/')
def hello_route():
    return render_template("photos.html", projects=projects.setup())


if __name__ == "__main__":
    app.run(debug = True, port=9090)
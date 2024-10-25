from flask import Flask, render_template

from api import api
from config import API_HOST, DATABASE_URI
from db import get_endpoints_from_db, init_db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.register_blueprint(api)

init_db(app)


@app.route("/")
def homepage():
    endpoints = get_endpoints_from_db()
    return render_template("index.html", endpoints=endpoints, api_host=API_HOST)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

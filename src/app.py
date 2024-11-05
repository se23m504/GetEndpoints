import logging
import signal
import sys

from flask import Flask, render_template
from waitress import serve

from api import api
from config import DATABASE_URI, LOG_LEVEL, SERVICE_IP, SERVICE_PORT
from db import get_endpoints_from_db, init_db
from register import register_service, unregister_service

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.register_blueprint(api)

init_db(app)


def handle_exit(*args):
    unregister_service()
    sys.exit(0)


signal.signal(signal.SIGTERM, handle_exit)


@app.route("/")
def homepage():
    endpoints = get_endpoints_from_db()
    return render_template("index.html", endpoints=endpoints, api_host=SERVICE_IP)


if __name__ == "__main__":
    logging.basicConfig(level=logging.getLevelName(LOG_LEVEL))

    register_service()

    try:
        serve(app, host=SERVICE_IP, port=SERVICE_PORT)
    finally:
        unregister_service()

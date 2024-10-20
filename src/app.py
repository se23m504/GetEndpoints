import os
from flask import Flask, render_template
from db import init_db, get_endpoints_from_db
from api import api
from dotenv import load_dotenv

load_dotenv()

DATABASE_URI = os.getenv('DATABASE')
API_HOST = os.getenv('API_HOST')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(api)

init_db(app)

@app.route('/')
def homepage():
    endpoints = get_endpoints_from_db()
    return render_template('index.html', endpoints=endpoints, api_host=API_HOST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

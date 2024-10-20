import os
from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from db import *
# from routes import register_routes
from dotenv import load_dotenv

load_dotenv()
DATABASE_URI = os.getenv('DATABASE')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

@app.route('/')
def homepage():
    endpoints = get_endpoints_from_db()
    return render_template('index.html', endpoints=endpoints)

@app.route('/api/endpoints', methods=['GET'])
def get_endpoints():
    endpoints = get_endpoints_from_db()
    return jsonify(endpoints)

@app.route('/api/endpoints/<int:endpoint_id>', methods=['GET'])
def get_endpoint(endpoint_id):
    endpoint = get_endpoint_by_id(endpoint_id)
    if endpoint:
        return jsonify(endpoint)
    else:
        abort(404)

@app.route('/api/endpoints/<int:endpoint_id>', methods=['PUT'])
def update_endpoint(endpoint_id):
    data = request.get_json()
    new_url = data.get('url')

    if new_url:
        update_endpoint_in_db(endpoint_id, new_url)
        return jsonify({"status": "success", "message": f"Endpoint {endpoint_id} updated to {new_url}"}), 200
    else:
        return jsonify({"status": "error", "message": "No new endpoint provided."}), 400

if __name__ == '__main__':
    app.run(host='windows.local', port=5000)

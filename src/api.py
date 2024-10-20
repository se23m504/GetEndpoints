from flask import Blueprint, abort, jsonify, request

from db import get_endpoint_by_id, get_endpoints_from_db, update_endpoint_in_db

api = Blueprint("api", __name__)


@api.route("/api/endpoints", methods=["GET"])
def get_endpoints():
    endpoints = get_endpoints_from_db()
    return jsonify(endpoints)


@api.route("/api/endpoints/<int:endpoint_id>", methods=["GET"])
def get_endpoint(endpoint_id):
    endpoint = get_endpoint_by_id(endpoint_id)
    if endpoint:
        return jsonify(endpoint)
    else:
        abort(404)


@api.route("/api/endpoints/<int:endpoint_id>", methods=["PUT"])
def update_endpoint(endpoint_id):
    data = request.get_json()
    new_url = data.get("url")

    if new_url:
        update_endpoint_in_db(endpoint_id, new_url)
        return (
            jsonify(
                {
                    "status": "success",
                    "message": f"Endpoint {endpoint_id} updated to {new_url}",
                }
            ),
            200,
        )
    else:
        return jsonify({"status": "error", "message": "No new endpoint provided."}), 400

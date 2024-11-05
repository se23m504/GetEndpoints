from flask import Blueprint, abort, jsonify, request

from db import (
    add_endpoint_to_db,
    delete_endpoint_from_db,
    get_endpoint_by_id,
    get_endpoint_by_url,
    get_endpoints_from_db,
    update_endpoint_in_db,
)
from utils import is_valid_url

api = Blueprint("api", __name__)


@api.route("/api/endpoints", methods=["GET"])
def get_endpoints():
    endpoints = get_endpoints_from_db()
    return jsonify(endpoints), 200


@api.route("/api/endpoints", methods=["POST"])
def create_endpoint():
    data = request.get_json()
    new_url = data.get("url")

    if new_url is None or not is_valid_url(new_url):
        return jsonify({"status": "error", "message": "Invalid or missing URL"}), 400

    existing_endpoint = get_endpoint_by_url(new_url)
    if existing_endpoint:
        return (
            jsonify(
                {
                    "status": "error",
                    "message": "Endpoint already exists",
                    "id": existing_endpoint["id"],
                }
            ),
            409,
        )

    endpoint_id = add_endpoint_to_db(new_url)
    return jsonify({"id": endpoint_id, "url": new_url}), 201


@api.route("/api/endpoints/<int:endpoint_id>", methods=["GET"])
def get_endpoint(endpoint_id):
    endpoint = get_endpoint_by_id(endpoint_id)
    if endpoint:
        return jsonify(endpoint), 200
    else:
        abort(404)


@api.route("/api/endpoints/<int:endpoint_id>", methods=["PUT"])
def update_endpoint(endpoint_id):
    data = request.get_json()
    new_url = data.get("url")

    if not new_url or not is_valid_url(new_url):
        return jsonify({"status": "error", "message": "Invalid or missing URL"}), 400

    updated = update_endpoint_in_db(endpoint_id, new_url)
    if updated:
        return "", 204
    else:
        return jsonify({"status": "error", "message": "Endpoint not found"}), 404


@api.route("/api/endpoints/<int:endpoint_id>", methods=["DELETE"])
def delete_endpoint(endpoint_id):
    deleted = delete_endpoint_from_db(endpoint_id)
    if deleted:
        return "", 204
    else:
        return jsonify({"status": "error", "message": "Endpoint not found"}), 404


@api.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

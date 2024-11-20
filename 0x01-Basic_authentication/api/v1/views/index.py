#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views
from models.user import User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """
    Handles GET requests to /api/v1/status.

    Returns:
        str: A JSON response indicating the status of the API.
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats() -> str:
    """
    Handles GET requests to /api/v1/stats.

    Returns:
        str: A JSON response containing the number of each objects
    """
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized', methods=["GET"], strict_slashes=False)
def unauthorized() -> str:
    """
    Handles GET requests to /api/v1/unauthorized.

    Returns:
        str: Triggers a 401 error using the abort function.
    """
    return abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden() -> str:
    """
    Handles GET requests to /api/v1/forbidden

    Returns:
        str: Triggers a 403 forbidden error using the abort function
    """
    return abort(403)

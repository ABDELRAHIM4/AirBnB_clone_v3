#!/usr/bin/python3
"""Create a new view for State objects that handles all default RESTFul API action"""
from flask import Flask, jsonify, abort
from models.state import State
from models import storage
from api.v1.views import app_views
@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_stats():
    """Create a new view for State"""
    stat = storage.all("State").values()
    return (jsonify([state.to_dict() for state in stat]))
@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get(state_id):
    """Retrieves a State object: GET"""
    state_get = storage.get("State", state_id)
    if state_get == None:
        abort(404)
    return (jsonify(state_get))
@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete(state_id):
    """Deletes a State object:"""
    state_get = storage.get("State", state_id)
    if state_get == None:
        abort(404)
    storage.delete(state_get)
    return ({})
@app_views.route('/states/<state_id>', methods=['POST'], strict_slashes=False)
def post(state_id):
    """Creates a State: POST"""
    if not request.get_json():
        abort(400, "Not a JSON")
    req = request.get_json()
    if "name" not in req:
        abort(400, "Missing name")
    state = storage.new("State")
    storage.save()
    return (jsonify(state), 201)
@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update(state_id):
    """Updates a State object"""
    state_get = storage.get("State", state_id)
    if state_get == None:
        abort(404)
    req = request.get_json()
    if not req:
        abort(400, "Not a JSON")
    for key, value in req.item():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(state, key, value)
    return (jsonify(state, 200))

#!/usr/bin/python3
"""Create a new view for State objects that handles all default RESTFul API action"""
from flask import Flask, jsonify, abort
from models.city import City
from models import storage
from api.v1.views import app_views
@app_views.route('/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
def get_city(state_id):
    """Create a new view for State"""
    state_get = storage.get("State", state_id)
    if state_get == None:
        abort(404)
    return (jsonify(state_get))
@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_cities(city_id):
    """Retrieves a City object: GET"""
    state_get = storage.get("City", city_id)
    if state_get == None:
        abort(404)
    return (jsonify(state_get))
@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """Deletes a City object:"""
    state_get = storage.get("City", city_id)
    if state_get == None:
        abort(404)
    storage.delete(state_get)
    return ({})
@app_views.route('/states/<state_id>/cities', methods=['POST'], strict_slashes=False)
def post_city(state_id):
    """Creates a City POST"""
    if not request.get_json():
        abort(400, "Not a JSON")
    req = request.get_json()
    if "name" not in req:
        abort(400, "Missing name")
    state = storage.new("City")
    storage.save()
    return (jsonify(state), 201)
@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """Updates a City object"""
    state_get = storage.get("City", city_id)
    if state_get == None:
        abort(404)
    req = request.get_json()
    if not req:
        abort(400, "Not a JSON")
    for key, value in req.item():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(state, key, value)
    return (jsonify(state, 200))

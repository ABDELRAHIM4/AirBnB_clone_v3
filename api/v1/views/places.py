#!/usr/bin/python3
"""Create a new view for Place objects"""
from flask import jsonify, request, abort
from models import storage
from api.v1.views import app_views

@app_views.route('/cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def get_places(city_id):
    """Retrieves a place object: GET"""
    state_get = storage.get("City", city_id)
    if state_get == None:
        abort(404)
    return (jsonify(state_get))

@app_views.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    """Retrieves a place object"""
    places = storage.get('Place', place_id)
    if places is None:
        abort(404)
    return jsonify(places.to_dict())

@app_views.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    """Deletes a place object"""
    places = storage.get('Place', place_id)
    if places is None:
        abort(404)
    storage.delete(places)
    return jsonify({}), 200

@app_views.route('/cities/<city_id>/places', methods=['POST'], strict_slashes=False)
def post_place(city_id):
    """Updates a place object"""
    state_get = storage.get("City", city_id)
    if state_get == None:
        abort(404)
    req = request.get_json()
    if not req:
        abort(400, "Not a JSON")
    if 'user_id' not in data:
        abort(400, "Missing user_id")
    for key, value in req.item():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(state_get, key, value)
    return (jsonify(state, 200))

@app_views.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    """Updates a place object"""
    places = storage.get('Place', user_id)
    if places is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(placess, key, value)
    storage.save()
    return jsonify(places.to_dict()), 200

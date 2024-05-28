#!/usr/bin/python3
"""Create a new view for State objects that handles all default RESTFul API action"""
from flask import Flask, jsonify, abort
from models.amentiy import Amenity
from models import storage
from api.v1.views import app_views
@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amen():
    """Create a new view for State"""
    amens = Amenity.all()
    return (jsonify([amen.to_dict() for amen in amens]))
@app_views.route('/amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def get_amen(amenity_id):
    """Retrieves a City object: GET"""
    state_get = storage.get("Amenity", amenity_id)
    if state_get == None:
        abort(404)
    return (jsonify(state_get))
@app_views.route('/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_amen(amenity_id):
    """Deletes a Amenity object:"""
    state_get = storage.get("Amenity", city_id)
    if state_get == None:
        abort(404)
    storage.delete(state_get)
    return ({}, 200)
@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def post_amen():
    """Creates a amenity POST"""
    if not request.get_json():
        abort(400, "Not a JSON")
    req = request.get_json()
    if "name" not in req:
        abort(400, "Missing name")
    amenity = storage.new("Amenity", **data)
    storage.save()
    return (jsonify(amenity.to_dict()), 201)
@app_views.route('/amenities/<amenity_id>', methods=['PUT'], strict_slashes=False)
def update_amen(amenity_id):
    """Updates a amenity object"""
    state_get = storage.get("Amenity", amenity_id)
    if state_get == None:
        abort(404)
    req = request.get_json()
    if not req:
        abort(400, "Not a JSON")
    for key, value in req.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(state_get, key, value)
    return (jsonify(state_get, 200))

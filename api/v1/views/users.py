#!/usr/bin/python3
"""Create a new view for User objects"""
from flask import jsonify, request, abort
from models import storage
from api.v1.views import app_views

@app_views.route('/users', methods=['GET'])
def get_users():
    """Retrieves the list of all user objects"""
    users = storage.all('User').values()
    return jsonify([user.to_dict() for user in users])

@app_views.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """Retrieves a user object"""
    users = storage.get('User', user_id)
    if users is None:
        abort(404)
    return jsonify(users.to_dict())

@app_views.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Deletes a user object"""
    users = storage.get('User', amenity_id)
    if users is None:
        abort(404)
    storage.delete(users)
    return jsonify({}), 200

@app_views.route('/users', methods=['POST'])
def create_user():
    """Creates a user"""
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    if 'name' not in data:
        abort(400, 'Missing name')
    amenity = storage.new('User', **data)
    storage.save()
    return jsonify(amenity.to_dict()), 201

@app_views.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """Updates a user object"""
    users = storage.get('User', user_id)
    if users is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(users, key, value)
    storage.save()
    return jsonify(users.to_dict()), 200

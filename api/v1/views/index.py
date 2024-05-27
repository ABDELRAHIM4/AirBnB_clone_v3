#!/usr/bin/python3
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from flask import jsonify
from api.v1.views import app_views
@app_views.route('/status', methods=['GET'])
def view():
	return jsonify({"status": "OK"})
@app_views.route('/stats', methods=['GET'])
def stats():
	stats = {}
	stats["amenities"] = storage.count(Amenity)
	stats["cities"] = storage.count(City)
	stats["places"] = storage.count(Place)
	stats["reviews"] = storage.count(Review)
	stats["states"] = storage.count(State)
	stats["users"] = storage.count(User)
	return (jsonify(stats))
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)

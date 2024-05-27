#!/usr/bin/python3
from flask import jsonify
from api.v1.views import app_views
@app_views.route('/status', methods=['GET'])
def view():
	return jsonify({"status": "OK"})

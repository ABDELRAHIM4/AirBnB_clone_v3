#!/usr/bin/python3
"""create a variable app, instance of Flask"""
import os
from flask import Flask
from models import storage
from api.v1.views import app_views
HBNB_MYSQL_USER = os.getenv("HBNB_MYSQL_USER", "hbnb_dev")
HBNB_MYSQL_PWD = os.getenv("HBNB_MYSQL_PWD", "hbnb_dev_pwd")
HBNB_MYSQL_HOST = os.getenv("HBNB_MYSQL_HOST", "localhost")
HBNB_MYSQL_DB = os.getenv("HBNB_MYSQL_DB", "hbnb_dev_db")
app = Flask(__name__)
app.register_blueprint(app_views)
@app.teardown_appcontext
def close_stroage(exception=None):
	"""declare a method to handle"""
	storage.close()
if __name__ == "__main__":
	""" run your Flask server"""
	host = os.getenv("HBNB_API_HOST", "0.0.0.0")
	port = os.getenv("HBNB_API_PORT", "5000")
	app.run(host=host, port=port, threaded=True)

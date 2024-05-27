#!/usr/bin/python3
from flask import Blueprint
<<<<<<< HEAD

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

=======
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
>>>>>>> storage_get_count
from api.v1.views.index import *

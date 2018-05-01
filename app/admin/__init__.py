# app/admin/__init__.py

# for admin page mgmt

from flask import Blueprint

admin = Blueprint('admin', __name__)

from . import views

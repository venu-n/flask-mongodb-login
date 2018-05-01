# app/auth/__init__.py

# for admin page mgmt

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views

# app/home/__init__.py

# for dashboard page mgmt

from flask import Blueprint

home = Blueprint('home', __name__)

from . import views

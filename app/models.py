from flask_login import UserMixin
from werkzeug.security import check_password_hash
from flask_mongoengine import MongoEngine, Document

from app import db, login_manager

class User(UserMixin, db.Document):
    meta = {'collection': 'users'}
    email = db.StringField(max_length=30)
    username = db.StringField()
    first_name = db.StringField()
    last_name = db.StringField()
    password = db.StringField()

@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()

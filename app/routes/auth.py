from flask import Blueprint, jsonify, flash, request
from flask_jwt_extended import create_access_token
from werkzeug import check_password_hash;

from app.models.user import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.post('/login')
def login():
  email = request.json.get("email", None)
  password = request.json.get("password", None)
  user = User.query.filter_by(email=email).first()
  if user and check_password_hash(user.password_digest, password):
    token = create_access_token(identity=user.id)
    return jsonify(status=200, access_token=token)
  else:
    return jsonify(status=422, error='Incorrect email or password')

@auth_bp.post('/register')
def register():
  email = request.json.get("email", None)
  password = request.json.get("password", None)
  existing_user = User.query.filter_by(email=email).first()
  if not existing_user:
    user = User.create(email, password)
    token = create_access_token(identity=user.id)
    return jsonify(status=200, access_token=token)
  else:
    return jsonify(status=422, error='User already exists')

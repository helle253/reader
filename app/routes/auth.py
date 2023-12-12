import json
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash;

from app.models.user import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.post('/login')
def login():
  parsed = json.loads(request.data);
  email = parsed["email"] or None
  password = parsed["password"] or None
  user = User.query.filter_by(email=email).first()
  if user and check_password_hash(user.password_digest, password):
    return jsonify(status=200, access_token=create_access_token(identity=user.id))
  else:
    return jsonify(status=422, error='Incorrect email or password')

@auth_bp.post('/register')
def register():
  parsed = json.loads(request.data);
  email = parsed["email"] or None
  password = parsed["password"] or None
  existing_user = User.query.filter_by(email=email).first()
  if not existing_user:
    user = User.create(email, password)
    token = create_access_token(identity=user.id)
    return jsonify(status=200, access_token=token)
  else:
    return jsonify(status=422, error='User already exists')

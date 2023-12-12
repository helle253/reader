from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.models.user import User

audio_bp = Blueprint('audio', __name__)

@audio_bp.get('/audio_clips')
@jwt_required()
def index():
  current_user_id = get_jwt_identity();
  print(User.query.get(current_user_id).audio_clips())
  return jsonify(audio_clips=User.query.get(current_user_id).audio_clips())

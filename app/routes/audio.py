from flask import Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.models.user import User

audio_bp = Blueprint('audio', __name__)

@audio_bp.get('/')
@jwt_required
def index():
  current_user_id = get_jwt_identity();

  User.query.get(id=current_user_id).first().audio_clips()

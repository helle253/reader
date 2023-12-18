import datetime
import json
from urllib.parse import urlparse
from flask import Blueprint, jsonify, request, stream_with_context
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.models.user import User
from app.persistence.s3_helpers import S3UploadProcess
from app.synthesis.synthesizer import Synthesizer
from app.synthesis.text_processing import chunk_text_selection

audio_clips_bp = Blueprint('audio_clips', __name__)

@audio_clips_bp.get('/audio_clips')
@jwt_required()
def index():
  current_user_id = get_jwt_identity();
  print(User.query.get(current_user_id).audio_clips())
  return jsonify(audio_clips=User.query.get(current_user_id).audio_clips())

@audio_clips_bp.post('/audio_clips')
@jwt_required()
@stream_with_context
def create():
  current_user_id = get_jwt_identity();
  parsed = json.loads(request.data);
  source_url = parsed["source_url"]
  parsed_url = urlparse(source_url)
  domain = parsed_url.netloc
  path = parsed_url.path.replace('/', '-')
  timestamp = datetime.datetime.now().isoformat()
  filename = f'{current_user_id}-{domain}-{path}-{timestamp}.mp3'

  text = parsed["text"] or None
  if text is None: raise Exception("Please provide input")

  def generator():
    with open(filename, 'ab') as f:
      for text_chunk in chunk_text_selection(text):
        for audio_chunk in Synthesizer().synthesize(text_chunk):
          f.write(audio_chunk)
          yield audio_chunk
  return generator()

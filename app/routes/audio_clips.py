import datetime
import json
from urllib.parse import urlparse
from flask import Blueprint, jsonify, request, stream_with_context
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.models.user import User
from app.persistence.s3_helpers import S3UploadProcess
from app.synthesis.synthesizer import Synthesizer

audio_clips_bp = Blueprint('audio_clips', __name__)

@audio_clips_bp.get('/audio_clips')
@jwt_required()
def index():
  current_user_id = get_jwt_identity();
  print(User.query.get(current_user_id).audio_clips())
  return jsonify(audio_clips=User.query.get(current_user_id).audio_clips())

@audio_clips_bp.post('/audio_clips')
@jwt_required()
def create():
  current_user_id = get_jwt_identity();
  parsed = json.loads(request.data);
  source_url = parsed["source_url"]
  parsed_url = urlparse(source_url)
  domain = parsed_url.netloc
  path = parsed_url.path.replace('/', '-')
  timestamp = datetime.datetime.now().isoformat()
  key = f'{current_user_id}/{domain}-{path}-{timestamp}.mp3'

  text = parsed["text"] or None
  if text is None: raise Exception("Please provide input")

  def generator():
    s3_process = S3UploadProcess(key)
    s3_process.spawn_worker()
    for chunk in Synthesizer().synthesize(text):
      s3_process.queue.put(chunk)
      yield chunk
    s3_process.no_more_incoming_data()
  return stream_with_context(generator)

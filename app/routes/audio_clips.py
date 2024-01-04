import datetime
import json
import io
from urllib.parse import urlparse
from flask import Blueprint, request, stream_with_context
from pydub import AudioSegment

from app.synthesis.synthesizer import Synthesizer
from app.synthesis.text_processing import process_text_selection

audio_clips_bp = Blueprint('audio_clips', __name__)

@audio_clips_bp.post('/audio_clips')
@stream_with_context
def create():
  parsed = json.loads(request.data);
  source_url = parsed["source_url"]
  parsed_url = urlparse(source_url)
  domain = parsed_url.netloc
  path = parsed_url.path.replace('/', '-')
  timestamp = datetime.datetime.now().isoformat()

  text = parsed["text"] or None
  if text is None: raise Exception("Please provide input")

  def generator():
    segment = AudioSegment.silent(100)
    for text_chunk in process_text_selection(text):
      with io.BytesIO() as f:
        for audio_chunk in Synthesizer().synthesize(text_chunk):
          f.write(audio_chunk)
          yield audio_chunk
        # Rewind buffer
        f.seek(0)
        segment = segment + AudioSegment.from_file(f)
      segment = segment + AudioSegment.silent(1000)
    filename = f'{domain}-{path}-{timestamp}.wav'
    segment.export(filename, format='wav')
  return generator()

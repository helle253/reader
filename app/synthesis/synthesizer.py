import os
from typing import Iterable
from pyht import Client, TTSOptions

from app.synthesis.text_processing import chunk_text_selection

class Synthesizer:
  def __init__(self, client: Client | None = None, options: TTSOptions | None = None):
    self.client = client or Client(
    user_id=os.getenv("PLAY_HT_USER_ID"),
    api_key=os.getenv("PLAY_HT_API_KEY"),
    )
    self.options = options or TTSOptions(voice=os.getenv("VOICE_URI"))

  def synthesize(self, text) -> Iterable[bytes]:
    for chunk in self.client.tts(
      text,
      self.options,
    ):
      yield chunk

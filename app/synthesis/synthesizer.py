import re
import os
from typing import Iterable
from pyht import Client, TTSOptions

class Synthesizer:
  def __init__(self, client: Client | None = None, options: TTSOptions | None = None):
    self.client = client or Client(
    user_id=os.getenv("PLAY_HT_USER_ID"),
    api_key=os.getenv("PLAY_HT_API_KEY"),
    )
    self.options = options or TTSOptions(voice=os.getenv("VOICE_URI"))

  def synthesize(self, text) -> Iterable[bytes]:
    preprocessed_text = self.preprocess(text)
    for chunk in self.client.tts(
      preprocessed_text,
      self.options,
    ):
      yield chunk


  def preprocess(self, text):
    # Remove multiple concurrent newlines.
    text = re.sub(r"\n{1,}", "\n", text)
    return text

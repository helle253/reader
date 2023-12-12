from urllib.parse import urlsplit;
from . import db;

class AudioClip(db.Model):
  __tablename__ = 'audio_clips'
  id = db.Column(db.Integer, primary_key=True)
  source_domain = db.Column(db.String(255))
  source_path = db.Column(db.String(1024))
  file_url = db.Column(db.String(2056), nullable=False)
  owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

  def __init__(self, source_url: str, file_url: str, owner_id: int):
    parsed = urlsplit(source_url)
    self.source_domain = parsed.netloc
    self.source_path = parsed.path
    self.file_url = file_url
    self.owner_id = owner_id

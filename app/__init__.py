
from dotenv import load_dotenv
from flask import Config, Flask
import nltk
nltk.download('punkt')

from app.routes.audio_clips import audio_clips_bp

load_dotenv()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(audio_clips_bp)
    return app

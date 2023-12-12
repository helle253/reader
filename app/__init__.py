import os
from dotenv import load_dotenv
from flask import Config, Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from pyht import Client

load_dotenv()

ht_client = Client(
    user_id=os.getenv("PLAY_HT_USER_ID"),
    api_key=os.getenv("PLAY_HT_API_KEY"),
)

db = SQLAlchemy()  # done here so that db is importable
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    conninfo = os.getenv("DB_CONNECTION")
    conninfo = conninfo.replace("postgresql", "postgresql+psycopg")
    app.config['SQLALCHEMY_DATABASE_URI'] = conninfo
    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.user import UserModel
    from app.models.audio_clip import AudioClipModel
    return app

import os
from dotenv import load_dotenv
from flask import Config, Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from pyht import Client

from app.routes.auth import auth_bp

load_dotenv()

ht_client = Client(
    user_id=os.getenv("PLAY_HT_USER_ID"),
    api_key=os.getenv("PLAY_HT_API_KEY"),
)

db = SQLAlchemy()  # done here so that db is importable
migrate = Migrate()
jwt = JWTManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    conninfo = os.getenv("DB_CONNECTION")
    conninfo = conninfo.replace("postgresql", "postgresql+psycopg")
    app.config['SQLALCHEMY_DATABASE_URI'] = conninfo
    app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from app.models.user import UserModel
    from app.models.audio_clip import AudioClipModel

    app.register_blueprint(auth_bp)
    return app

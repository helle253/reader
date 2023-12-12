from dotenv import load_dotenv
from flask import Flask, request
from flask_migrate import Migrate
from pyht import Client
import os

from persistence.db import DB

load_dotenv()

ht_client = Client(
    user_id=os.getenv("PLAY_HT_USER_ID"),
    api_key=os.getenv("PLAY_HT_API_KEY"),
)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_CONNECTION")
DB.initialize(app)
migrate = Migrate(app, DB.get())

@app.route("/")
def hello():
    return "Hello, World!"

@app.get("/web/audio")
def web_audio_index():
    return "Index retrieved"

@app.post("/web/audio")
def web_audio_create():
    text = request.get_json()['text']
    return f"Audio {request.get_json()['text']} created!"

@app.get("/web/audio/<id>")
def web_audio_show(id):
    return f"Audio {id} retrieved!"


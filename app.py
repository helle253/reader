from dotenv import load_dotenv
from flask import Flask, request
from pyht import Client
import os

load_dotenv()

ht_client = Client(
    user_id=os.getenv("PLAY_HT_USER_ID"),
    api_key=os.getenv("PLAY_HT_API_KEY"),
)
app = Flask(__name__)

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

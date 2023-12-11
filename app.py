# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/web/audio", methods = ['GET', 'POST'])
def audio_index():
    return "Audio created!"

@app.route("/web/audio/<ID>", methods = ['GET'])
def get_audio(ID):
    return "Audio {ID} retrieved!"

@app.route("/files/audio", methods = ['GET', 'POST'])
def audio_index():
    return "Audio created!"

@app.route("/files/audio/<ID>", methods = ['GET'])
def get_audio(ID):
    return "Audio {ID} retrieved!"

import face_recognition
import requests
from PIL import Image
import io
import numpy as np
from flask import Flask
from flask import request
import os
import json
app = Flask(__name__)

if os.environ.get("ENV") == "docker":
    IMAGE_URL = "http://file_server/"
else :
    IMAGE_URL = "http://localhost:8080/"

@app.route("/")
def index():
    return "<h1>Welcome! Make a Post Request</h1>"

@app.route("/add", methods=["POST"])
def add_photo():
    if request.method == "POST":
        data = request.get_json()
        file = request.files["file"]
        file.save(os.path.join("uploads",file.filename))
#         print(file.filename)
    return {"id":file.filename}

@app.route("/detect", methods=["POST"])
def detect_face():
    if request.method == "POST":
        name = request.form["id"]
        file = request.files["file"]
        unknown_image = Image.open(io.BytesIO(file.read()))
        unknown_image = np.array(unknown_image)
        image = requests.get(IMAGE_URL + name).content
        known_image = np.array(Image.open(io.BytesIO(image)))
        known_image = known_image[:,:,:3]
        unknown_image = unknown_image[:,:,:3]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
        know_encoding = face_recognition.face_encodings(known_image)[0]
        result = face_recognition.compare_faces([know_encoding],unknown_encoding)
        return {"data":{"result": bool(result[0])}}
    return {"done":True}

if __name__ == "__main__":
    app.run(host='0.0.0.0')

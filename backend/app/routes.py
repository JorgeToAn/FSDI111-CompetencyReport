from urllib import response
from flask import Flask, request

app = Flask(__name__)

from app.database import notes

RESPONSE = {
    "status": "OK"
}


# ---------- GET ----------
@app.get("/notes")
def get_notes():
    response = dict(RESPONSE)
    response["notes"] = notes.scan()
    return response


@app.get("/note/<int:pk>")
def get_note(pk):
    response = dict(RESPONSE)
    response["note"] = notes.select_by_id(pk)
    return response


# --------- POST ----------
@app.post("/notes")
def create_note():
    note_body = request.json
    notes.create(note_body)
    return "", 204


# --------- PUT ----------
@app.put("/note/<int:pk>")
def update_note(pk):
    note_body = request.json
    notes.update(note_body, pk)
    return "", 204


@app.delete("/note/<int:pk>")
def delete_note(pk):
    notes.delete(pk)
    return "", 204
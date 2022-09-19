from flask import Flask, render_template, request
import requests

app = Flask(__name__)
BACKEND_URL = "http://127.0.0.1:5001/notes"


@app.get("/")
def index():
    response = requests.get(BACKEND_URL)
    scan_data = response.json().get("notes")
    return render_template("index.html", notes=scan_data)


@app.get("/note/<pk>")
def view_note(pk):
    url = "%s/%s" % (BACKEND_URL, pk)
    response = requests.get(url)
    note_data = response.json().get("note")
    return render_template("note.html", note=note_data[0])


@app.get("/create")
def get_create_form():
    return render_template("new_note.html")


@app.post("/create")
def create_note():
    form_data = request.form
    new_note = {
        "title": form_data.get("title"),
        "subtitle": form_data.get("subtitle"),
        "body": form_data.get("body")
    }
    response = requests.post(BACKEND_URL, json=new_note)
    if response.status_code == 204:
        return render_template("success.html")
    else:
        return render_template("fail.html")


@app.get("/update/<pk>")
def get_update_form(pk):
    url = "%s/%s" % (BACKEND_URL, pk)
    response = requests.get(url)
    note_data = response.json().get("note")
    return render_template("update_note.html", note=note_data[0])


@app.post("/update/<pk>")
def update_note(pk):
    form_data = request.form
    updated_note = {
        "title": form_data.get("title"),
        "subtitle": form_data.get("subtitle"),
        "body": form_data.get("body")
    }
    url = "%s/%s" % (BACKEND_URL, pk)
    response = requests.put(url, json=updated_note)
    if response.status_code == 204:
        return render_template("success.html")
    else:
        return render_template("fail.html")


@app.post("/delete/<pk>")
def delete_note(pk):
    url = "%s/%s" % (BACKEND_URL, pk)
    response = requests.delete(url)
    if response.status_code == 204:
        return render_template("success.html")
    else:
        return render_template("fail.html")

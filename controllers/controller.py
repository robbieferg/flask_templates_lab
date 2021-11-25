from flask import render_template, request
from app import app
from models.event import Event
from models.event_list import events


@app.route("/")
def index():
    return render_template("index.html", title = "Home", events = events)

@app.route("/add_event")
def add_event():
    return render_template("add_event.html", title = "Add Event")
    
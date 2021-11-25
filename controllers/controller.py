from flask import render_template, request
from app import app
from models.event import Event
from models.event_list import *


@app.route("/")
def index():
    return render_template("index.html", title = "Home", events = events)

@app.route("/add_event")
def add_event_page():
    return render_template("add_event.html", title = "Add Event")

@app.route("/add_event", methods = ["POST"])
def add_new_event():
    event_date = request.form["date"]
    event_name = request.form["name"]
    event_number_of_guests = request.form["number_of_guests"]
    event_room_location = request.form["room_location"]
    event_description = request.form["description"]

    new_event = Event(event_date, event_name, event_number_of_guests, event_room_location, event_description)
    add_event(new_event)
    return render_template("index.html", title = "Home", events = events)
    
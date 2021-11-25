from flask import render_template, request
from app import app
# from models.event import Event


@app.route("/")
def index():
    return "hello world"
from flask import Flask, request, session, redirect, render_template
from flask_api import status
from werkzeug.serving import run_simple
import bcrypt
import pymysql.cursors
import json
import os
import requests
import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


# open up the config file
with open("config.json") as config:
    config = json.loads(config.read())

app = Flask(__name__, template_folder='templates')
app.debug = config["debug"]
app.secret_key = config["session-secret"]


@app.route("/fb_callback", methods=["GET", "POST"])
def index():
    return "hello"


if __name__ == "__main__":
    run_simple(config["website"], config["port"], app,
               use_reloader=True, use_debugger=True, use_evalex=True)
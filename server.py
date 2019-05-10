import os
from datetime import datetime as dt
from random import randrange

from bottle import route, run, static_file, view, template

@route("/")
def index():
    data = {
        "developer_name": "Sandzhi",
        "developer_organization": "Barg company"
    }
    return template("index", data = data)


@route("/static/<filename>") # TODO JS SCRIPT
def send_js(filename):
    return static_file(filename, root="./static/")


@route("/static/<filename>")  # TODO JS SCRIPT
def send_css(filename):
    return static_file(filename, root="./static/")


route("/api/roll/<some_id>")
def example_api_response(some_id):
    return {
        "requested_id":some_id,
        "random_number": randrange(some_id)
    }

if os.environ.get("PYW_ODIN") == "heroku":
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host="localhost", port=8080, debug=True)




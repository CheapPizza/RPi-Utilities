"""
Simple as possible JSON POST API on flask

pip install Flask

sudo apt install python3-flask

"""

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/test_route", methods=["POST"])
def hello_world():
    print(request.get_json())
    return jsonify({"test": "response"})

app.run()

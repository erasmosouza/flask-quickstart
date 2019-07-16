from flask import jsonify
from src import app


@app.route('/')
def index():
    return jsonify(message="hello, my new world!!!")

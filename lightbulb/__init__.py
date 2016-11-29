from flask import Flask, jsonify

from . import sensors

app = Flask(__name__)


@app.route('/echo')
def index():
    return 'Hello World!'


@app.route('/sensors')
def read_sensors():
    return jsonify(sensors.fetch_data())

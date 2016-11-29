from flask import Flask, jsonify
from flask import render_template

from . import sensors

app = Flask(__name__)


@app.route('/echo')
def echo():
    return 'Hello World!'


@app.route('/sensors')
def read_sensors():
    return jsonify(sensors.fetch_data())


@app.route('/')
def dashboard():
    return render_template('dashboard.html')

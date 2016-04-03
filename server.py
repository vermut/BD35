# -*- coding: utf-8 -*-
"""
    jQuery Example
    ~~~~~~~~~~~~~~
    A simple application that shows how Flask and jQuery get along.
    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from time import strftime

from flask import Flask, render_template, request

app = Flask(__name__)

my_clients = {}
my_data = {}


@app.route('/clients')
def clients():
    return render_template('clients.html', clients=my_clients, data=my_data)


@app.route('/report/<id>/<int:distance>/<int:voltage>')
def report(id, distance, voltage):
    my_data[id] = {'dist': distance, 'time': strftime("%a, %d %b %Y %H:%M:%S +0000"), 'voltage': voltage}

    return 'OK!'


@app.route('/sensor_record', methods=['POST'])
def sensor_report():
    content = request.get_json(force=True)
    my_data[content['id']] = {'dist': content['distance'],
                              'time': strftime("%a, %d %b %Y %H:%M:%S +0000"),
                              'voltage': content['voltage'] / 1000.0}

    return 'OK!'


@app.route('/sensor_register', methods=['POST'])
def sensor_register():
    content = request.get_json(force=True)
    my_clients[content['id']] = {'startup_distance': content['startup_distance']}
    return 'Registered!'


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)

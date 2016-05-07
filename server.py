# -*- coding: utf-8 -*-
"""
    jQuery Example
    ~~~~~~~~~~~~~~
    A simple application that shows how Flask and jQuery get along.
    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
import json
import urllib2
from time import strftime

from flask import Flask, render_template, request

import media
# from flask.ext.sqlalchemy import SQLAlchemy
from state.Game import Game, Team
from sensors import map_gate, map_name

app = Flask(__name__, static_url_path='/static')


class Dungeon():
    def __init__(self):
        self.clients = {}
        self.data = {}

        self.team1 = Team()
        self.team2 = Team()

        self.game = None # Game(self.team1)

    def team1_start(self):
        self.game = Game(self.team1)

    def team2_start(self):
        self.game = Game(self.team2)

    def trigger(self, gate):
        self.game.trigger(gate)

    def rewind(self):
        self.game.rewind()

    def update_sensor(self, id, content):
        self.data[id] = content

        if id not in self.clients:
            self.clients[id] = {'gates': map_name(id),
                                'max_voltage': content['voltage'],
                                'voltage': content['voltage']}
        else:
            self.clients[id]['voltage'] = content['voltage']


@app.route('/clients')
def clients():
    return render_template('clients.html', dungeon=dungeon)


@app.route('/sensor_record', methods=['POST'])
def sensor_report():
    content = request.get_json(force=True)
    dungeon.update_sensor(content['id'], {'gates': map_name(content['id']),
                                          'dist1': content['distance'],
                                          'dist2': content['distance2'],
                                          'time': strftime("%a, %d %b %Y %H:%M:%S +0000"),
                                          'voltage': content['voltage'] / 1000.0})

    gate = map_gate(content)
    if gate:
        # media.door.play()
        dungeon.trigger(gate)

    # req = urllib2.Request(
    #     'http://search-dungeon-qcc7an54euyyq4vnstm2j673ve.us-east-1.es.amazonaws.com/dungeon/sensor_record')
    # req.add_header('Content-Type', 'application/json')
    # urllib2.urlopen(req, json.dumps(content))

    return 'OK!'


# @app.route('/sensor_register', methods=['POST'])
# def sensor_register():
#     content = request.get_json(force=True)
#     dungeon.clients[content['id']] = {'startup_distance': content['startup_distance']}
#     return 'Registered!'


@app.route('/team1_start')
def team1_start():
    dungeon.team1_start()
    return "OK"


@app.route('/team2_start')
def team2_start():
    dungeon.team2_start()
    return "OK"


@app.route('/go/<gate>')
def go(gate):
    dungeon.trigger(gate)
    return "OK"


@app.route('/rewind')
def rewind():
    dungeon.rewind()
    return "OK"


@app.route('/')
def index():
    return render_template('index.html')


dungeon = Dungeon()

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)

# -*- coding: utf-8 -*-
"""
    jQuery Example
    ~~~~~~~~~~~~~~
    A simple application that shows how Flask and jQuery get along.
    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from time import strftime

import pyglet
from flask import Flask, render_template, request

# from flask.ext.sqlalchemy import SQLAlchemy
from state.Game import Game, Team
from sensors import map_gate

app = Flask(__name__, static_url_path='/static')
door = pyglet.media.load('static/jail_cell_door.wav', streaming=False)


class Dungeon():
    def __init__(self):
        self.clients = {}
        self.data = {}

        self.team1 = Team()
        self.team2 = Team()

        self.game = Game(self.team1)

    def team1_start(self):
        self.game = Game(self.team1)

    def team2_start(self):
        self.game = Game(self.team2)

    def trigger(self, gate):
        self.game.trigger(gate)

    def rewind(self):
        self.game.rewind()


@app.route('/clients')
def clients():
    return render_template('clients.html', dungeon=dungeon)


@app.route('/sensor_record', methods=['POST'])
def sensor_report():
    content = request.get_json(force=True)
    dungeon.data[content['id']] = {'dist1': content['distance'],
                                      'dist2': content['distance2'],
                                      'time': strftime("%a, %d %b %Y %H:%M:%S +0000"),
                                      'voltage': content['voltage'] / 1000.0}

    gate = map_gate(content)
    if gate:
        door.play()
        dungeon.trigger(gate)

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

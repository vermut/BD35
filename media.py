import pyglet

p = pyglet.media.Player()
door = pyglet.media.load('static/jail_cell_door.wav', streaming=False)
death = pyglet.media.load('static/FAIL.mp3', streaming=False)


def intro():
    _play('intermission.mp3')


def dinner():
    _play('dinner.mp3')


def puberty():
    _play('puberty.mp3')


def work():
    _play('work.mp3')


def bedroom():
    _play('bedroom.mp3')


def mountains():
    _play('mountains.mp3')


def the_end():
    _play('TheEnd.mp3')


def _play(mp3):
    snd = pyglet.media.load('static/' + mp3)
    looper = pyglet.media.SourceGroup(snd.audio_format, None)
    looper.loop = True
    looper.queue(snd)

    p.delete()
    p.queue(looper)
    p.play()

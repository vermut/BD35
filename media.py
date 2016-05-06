import pyglet

p = pyglet.media.Player()
door = pyglet.media.load('static/jail_cell_door.wav', streaming=False)
death = pyglet.media.load('static/nmh_scream1.wav', streaming=False)


def intro():
    snd = pyglet.media.load('static/intermission.mp3')
    looper = pyglet.media.SourceGroup(snd.audio_format, None)
    looper.loop = True
    looper.queue(snd)

    p.delete()
    p.queue(looper)
    p.play()


def room1():
    snd = pyglet.media.load('static/room1.mp3')
    looper = pyglet.media.SourceGroup(snd.audio_format, None)
    looper.loop = True
    looper.queue(snd)

    p.delete()
    p.queue(looper)
    p.play()


def room2():
    snd = pyglet.media.load('static/room2.mp3')
    looper = pyglet.media.SourceGroup(snd.audio_format, None)
    looper.loop = True
    looper.queue(snd)

    p.delete()
    p.queue(looper)
    p.play()

import pyglet

from Death import Death

door = pyglet.media.load('static/jail_cell_door.wav', streaming=False)
death = pyglet.media.load('static/nmh_scream1.wav', streaming=False)


class LevelState:
    def __init__(self, team):
        self.A = list("-")
        self.B = list("?")
        self.C = list("?")
        self.D = list("?")
        self.E = list("-")
        self.team = team

    def open_gate(self, gate):
        vars(self)[gate][0] = '+'

    def go(self, gate):
        if vars(self)[gate][0] is "-":
            return self.death(gate)

        if vars(self)[gate][0] is "?":
            special = getattr(self, 'special_'+gate)
            return special()

        if len(vars(self)[gate]) > 1:
            self.open_gate(vars(self)[gate][1])
        return self

    def status(self):
        return [(k + ' '.join(v)) for k, v in sorted(vars(self).items()) if len(k) == 1]

    def gates(self):
        return {
            "A": {'x': 830, 'y': 324, 'style': self._class_for('A')},
            "B": {'x': 857, 'y': 200, 'style': self._class_for('B')},
            "C": {'x': 1020, 'y': 200, 'style': self._class_for('C')},
            "D": {'x': 988, 'y': 157, 'style': self._class_for('D')},
            "E": {'x': 700, 'y': 100, 'style': self._class_for('E')},
        }.items()

    def _class_for(self, gate):
        if gate == 'B' and not self.team.canGoViaBravo: return 'my-red'
        if gate == 'C' and not self.team.canGoViaCharlie: return 'my-red'
        if gate == 'D' and self.team.canGoViaCharlie: return 'my-red'

        return 'my-red' if vars(self)[gate][0] is "-" else ''

    def death(self, gate):
        death.play()
        return Death(gate)

    def special_B(self):
        if not self.team.canGoViaBravo:
            return self.death('B')

        return self

    def special_C(self):
        if not self.team.canGoViaCharlie:
            return self.death('C')

        # Can go directly to E if C was open
        self.open_gate('E')
        return self

    def special_D(self):
        if self.team.canGoViaCharlie:
            return self.death('C!>D')

        # Must pass via D is B was open
        self.open_gate('E')
        return self

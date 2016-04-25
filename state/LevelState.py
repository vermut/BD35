from Death import Death


class LevelState:
    def __init__(self):
        self.A = list("+B")
        self.B = list("-C")
        self.C = list("-")

    def open_gate(self, gate):
        vars(self)[gate][0] = '+'

    def go(self, gate):
        if vars(self)[gate][0] is "-":
            return Death(gate)

        if vars(self)[gate][0] is "?":
            print "HANDLE_SPECIAL"

        self.open_gate(vars(self)[gate][1])
        return self

    def status(self):
        return sorted(vars(self).items())

    def gates(self):
        return {
            "A": {'x': 10, 'y': 10, 'style': self._class_for('A')},
            "B": {'x': 30, 'y': 30, 'style': self._class_for('B')},
            "C": {'x': 60, 'y': 60, 'style': self._class_for('C')},
        }.items()

    def _class_for(self, gate):
        return 'my-red' if vars(self)[gate][0] is "-" else ''

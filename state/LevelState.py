import media


from Death import Death



class LevelState:
    def __init__(self, team):
        self.A = list("-")
        self.B = list("?")  # B or C
        self.C = list("?")  # B or C
        self.D = list("?")  # D if B
        self.E = list("-F")
        self.F = list("-H")
        self.G = list("-")
        self.H = list("-A")  # For fun
        self.I = list("-K")
        self.J = list("?")  # 1 +India 2 + L+N
        self.K = list("-G")  # For fun
        self.L = list("?")  # 15 sec with L+N
        self.M = list("?")  # 3 times M<->O
        self.N = list("?")  # 15 sec with L+N
        self.O = list("?")  # 3 times M<->O
        self.P = list("-")
        self.Q = list("?")  # Locks everything until until they "come back"
        self.S = list("-")
        self.R = list("-")
        self.T = list("-")
        self.team = team

    def open_gate(self, gate):
        vars(self)[gate][0] = '+'

    def go(self, gate):
        if vars(self)[gate][0] is "-":
            return self.death(gate)

        if vars(self)[gate][0] is "?":
            special = getattr(self, 'special_' + gate)
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
        media.death.play()
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

    def special_J(self):
        return self

    def special_L(self):
        return self

    def special_M(self):
        return self

    def special_N(self):
        return self

    def special_O(self):
        return self

    def special_Q(self):
        return self

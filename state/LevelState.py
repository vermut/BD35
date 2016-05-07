import time

import media
from Death import Death


class LevelState:
    def __init__(self, team):
        self.A = list("-")
        self.B = list("+D?")  # ?=B or C + music
        self.C = list("+E?")  # ?=B or C + music
        self.D = list("-E")  # D if B
        self.E = list("-F?")  # ?=music
        self.F = list("-H")
        self.G = list("-")
        self.H = list("-J?")  # ?=music
        self.I = list("-K")
        self.J = list("-I?")  # 1 +India 2 + L+N
        self.K = list("-J?")  # Notifies Juliet
        self.L = list("-L?")  # 15 sec with L+N (and locks everything)
        self.M = list("-M?")  # 3 times M<->O
        self.N = list("-N?")  # 15 sec with L+N
        self.O = list("-O?")  # 3 times M<->O
        self.P = list("-")
        self.Q = list("-Q?")  # Locks everything until they "come back"
        self.S = list("-S?")
        self.R = list("-")
        self.T = list("-")
        self.team = team
        self.music = media.dinner

        self.bravo_is_safe = False
        self.charlie_is_safe = False

        self.m_count = 0
        self.o_count = 0

        self.last_q = 0

        self.last_gate = None

    def open_gate(self, gate):
        vars(self)[gate][0] = '+'

    def go(self, gate):
        self.last_gate = gate
        if vars(self)[gate][0] is "-":
            return self.death(gate)

        if len(vars(self)[gate]) > 1:
            self.open_gate(vars(self)[gate][1])

        if len(vars(self)[gate]) > 2 and vars(self)[gate][2] is "?":
            special = getattr(self, 'special_' + gate)
            return special()

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
            "F": {'x': 575, 'y': 205, 'style': self._class_for('F')},
            "G": {'x': 540, 'y': 175, 'style': self._class_for('G')},
            "H": {'x': 460, 'y': 313, 'style': self._class_for('H')},
            "I": {'x': 430, 'y': 355, 'style': self._class_for('I')},
            "J": {'x': 300, 'y': 320, 'style': self._class_for('J')},
            "K": {'x': 275, 'y': 380, 'style': self._class_for('K')},
            "L": {'x': 430, 'y': 205, 'style': self._class_for('L')},
            "M": {'x': 445, 'y': 150, 'style': self._class_for('M')},
            "N": {'x': 270, 'y': 205, 'style': self._class_for('N')},
            "O": {'x': 260, 'y': 150, 'style': self._class_for('O')},
            "P": {'x': 300, 'y': 100, 'style': self._class_for('P')},
            "Q": {'x': 320, 'y': 40, 'style': self._class_for('Q')},
            "S": {'x': 170, 'y': 150, 'style': self._class_for('S')},
            "R": {'x': 130, 'y': 205, 'style': self._class_for('R')},
            "T": {'x': 750, 'y': 292, 'style': self._class_for('T')},
        }.items()

    def _class_for(self, gate):
        if gate == 'B' and not (self.team.canGoViaBravo or self.bravo_is_safe): return 'my-red'
        if gate == 'C' and not (self.team.canGoViaCharlie or self.charlie_is_safe): return 'my-red'

        return 'my-red' if vars(self)[gate][0] is "-" else ''

    def death(self, gate):
        media.death.play()
        return Death(gate)

    def special_B(self):
        if not (self.team.canGoViaBravo or self.bravo_is_safe):
            self.team.canGoViaBravo = True
            self.team.canGoViaCharlie = False
            return self.death('B')

        self.bravo_is_safe = True
        self.team.canGoViaBravo = False
        self.team.canGoViaCharlie = True

        self.music = media.puberty
        return self

    def special_C(self):
        if not (self.team.canGoViaCharlie or self.charlie_is_safe):
            self.team.canGoViaBravo = False
            self.team.canGoViaCharlie = True
            return self.death('C')

        self.charlie_is_safe = True
        self.team.canGoViaBravo = True
        self.team.canGoViaCharlie = False

        self.music = media.puberty
        return self

    def special_E(self):
        self.music = media.work
        return self

    def special_H(self):
        self.music = media.bedroom
        return self

    def special_J(self):
        return self

    def special_L(self):
        # Todo set timer
        self.music = media.mountains
        return self

    def special_N(self):
        # Todo cancel timer
        self.music = media.mountains
        return self

    def special_M(self):
        if self.m_count == self.o_count or self.m_count == self.o_count - 1:
            self.m_count += 1

        if self.m_count == self.o_count == 3:
            media.door.play()  # Podskazka, chto vse ok
            self.open_gate('Q')

        return self

    def special_O(self):
        if self.o_count == self.m_count or self.o_count == self.m_count - 1:
            self.o_count += 1

        if self.m_count == self.o_count == 3:
            media.door.play()  # Podskazka, chto vse ok
            self.open_gate('Q')

        return self

    def special_Q(self):
        if self.last_q and time.time() - self.last_q > 20:
            self.open_gate('R')
            self.open_gate('S')
            media.door.play()  # Podskazka, chto vse ok

        self.last_q = time.time()
        return self

    def special_S(self):
        self.music = media.the_end
        return self

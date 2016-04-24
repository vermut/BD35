import copy

from Death import Death


class LevelState:
    def __init__(self):
        self.A = list("+B")
        self.B = list("-C")
        self.C = list("-")

    def openGate(self, gate):
        vars(self)[gate][0] = '+'

    def go(self, gate):
        if vars(self)[gate][0] is not "+":
            # print "!!! DEAD"
            return Death()

        self.openGate(vars(self)[gate][1])
        return self

    def status(self):
        print sorted(vars(self).items())

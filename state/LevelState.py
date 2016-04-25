from Death import Death


class LevelState:
    def __init__(self):
        self.A = list("+B")
        self.B = list("-C")
        self.C = list("-")

    def openGate(self, gate):
        vars(self)[gate][0] = '+'

    def go(self, gate):
        if vars(self)[gate][0] is "-":
            return Death()


        if vars(self)[gate][0] is "?":
            print "HANDLE_SPECIAL"

        self.openGate(vars(self)[gate][1])
        return self

    def status(self):
        print sorted(vars(self).items())

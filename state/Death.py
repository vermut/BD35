import media


class Death:
    def __init__(self, cause):
        self.cause = cause
        self.music = media.intro
        self.last_gate = "Death by " + cause

    def status(self):
        return "Death by " + self.cause

    def gates(self):
        return {}

    def go(self, gate):
        return self

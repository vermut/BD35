class Death:
    def __init__(self, cause):
        self.cause = cause

    def status(self):
        return "Death by " + self.cause

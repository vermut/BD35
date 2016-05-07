import copy

from state.LevelState import LevelState


class Team():
    def __init__(self):
        self.canGoViaBravo = False
        self.canGoViaCharlie = False


class Game():
    def __init__(self, team):
        self.stateHistory = []
        self.team = team
        self.state = LevelState(team)

    def trigger(self, gate):
        self.stateHistory.append(copy.deepcopy(self.state))
        self.state = self.state.go(gate)
        #todo change music if needed
        #todo don't trigger if same door

    def rewind(self):
        if len(self.stateHistory) > 0:
            self.state = self.stateHistory.pop()

        #todo change music



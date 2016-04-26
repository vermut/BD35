import copy

from state.LevelState import LevelState


class Team():
    def __init__(self):
        self.BravoIsHungry = True
        self.CharlieIsHungry = True


class Game():
    def __init__(self, team):
        self.stateHistory = []
        self.team = team
        self.state = LevelState()

    def trigger(self, gate):
        self.stateHistory.append(copy.deepcopy(self.state))
        self.state = self.state.go(gate)

    def rewind(self):
        if len(self.stateHistory) > 0:
            self.state = self.stateHistory.pop()

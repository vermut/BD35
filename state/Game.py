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
        music = self.state.music
        self.stateHistory.append(copy.deepcopy(self.state))
        self.state = self.state.go(gate)

        if self.state.music is not music:
            self.state.music()

    def rewind(self):
        music = self.state.music
        if len(self.stateHistory) > 0:
            self.state = self.stateHistory.pop()

        if self.state.music is not music:
            self.state.music()




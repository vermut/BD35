import copy

from state.LevelState import LevelState


class Team():
    def __init__(self, myname):
        self.canGoViaBravo = False
        self.canGoViaCharlie = False
        self.name = myname


class Game():
    def __init__(self, team):
        self.stateHistory = []
        self.team = team
        self.state = LevelState(team)
        self.state.music()

    def trigger(self, gate):
        if self.state.last_gate is gate:
            self.state.go(gate)
            return

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

from LevelState import LevelState

state = LevelState()
state.go('B').status()

state = LevelState()
state.status()
state.go('A').status()
state.go('B').status()

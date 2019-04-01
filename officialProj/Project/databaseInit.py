import pickle
import os
import sqlite3
import jsonpickle
		
# region stateFunctions
# Checks if the state file exists
# Creates the state file if it doesn't exist
# Then returns hash map representing the state file
def initializeState():
	filepath = "state"
	if not os.path.isfile(filepath):
		saveState(createState())
	return loadState()


def createState():
	return {"currentAppetizerNum" : 0}


def saveState(state):
	filepath = "state"
	outfile = open(filepath, "wb")
	pickle.dump(state, outfile)
	outfile.close()


def loadState():
	filepath = "state"
	infile = open(filepath, "rb")
	output = pickle.load(infile)
	infile.close()
	return output


def getState(attr):
	if not attr in state:
		state[attr] = 0
		saveState(state)
	return state[attr]


def setState(attr, value):
	state[attr] = value
	saveState(state)


def getStateCounter(attr):
	output = getState(attr)
	setState(attr, output + 1)
	return output
# endregion


state = initializeState()


# region utility functions


def toJSON(o):
	return jsonpickle.encode(o)


# endregion

# region database interaction
# database procedures


def initializeDatabase():
	filepath = 'example.db'
	if not os.path.isfile(filepath):
		out = sqlite3.connect('example.db')

		initfile = "DatabaseInitialization.sql"
		infile = open(initfile, 'r')
		sql = infile.read()
		infile.close()

		out.executescript(sql)
	else:
		out = sqlite3.connect('example.db')

	return out


# endregion


conn = initializeDatabase()



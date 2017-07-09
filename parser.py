# CS467 Parser.py
# Group Hydra

# VERB + OBEJCT
# MOVE + direction

validVerb = ["look", "go", "take"]
menuVerb = ["start", "resume", "save"]
singleVerb = ["help", "inventory"]

# verbs method ---------------------------------------

# repeats the long form explanation of the room
def lookItem(item):
	print "look", item

def goDirection(direction):
	print "go", direction

#acquire an object, putting it into your inventory
def takeItem(item):
	print "take", item

#list a set of verbs the game understands
def helpUser():
	print "help"
#
def checkInventory():
	print "check checkInventory"

def startGame():
	print "start new game"

def resumeGame():
	print "resume prev game"

def saveGame():
	print "save the game"

#--------------------------------------------------------


dispatch = {"start": startGame, "resume": resumeGame, "save": saveGame, 
			"look": lookItem, "go": goDirection, "take": takeItem, "help": helpUser,
			"inventory": checkInventory}

# helper ------------------------------------------------
def isVerbValid(verb):
	return verb in validVerb

def isMenuVerb(verb):
	return verb in menuVerb

def isSingleVerb(verb):
	return verb in singleVerb
#--------------------------------------------------------

def commandParsing(userInput):
	#print "this is the input", userInput
	#required verbs and phrases
	verb = userInput.split()[0]
	#check the verb is in the list
	if isVerbValid(verb) or isMenuVerb(verb) or isSingleVerb(verb):
		if isMenuVerb(verb) or isSingleVerb(verb):
			dispatch[verb]()
		else:
			item = userInput.split()[1]
			dispatch[verb](item)
	else:
		print "usage: VERB OBJECT"
	return

def main():
	command = raw_input("> ")
	commandParsing(command)

if __name__ == "__main__":
    main()
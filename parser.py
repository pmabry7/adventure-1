# CS467 Parser.py
# Group Hydra

# VERB + OBEJCT
# MOVE + direction

actionVerb = ["look", "go", "take"]
#preposition = ["to", ]
menuVerb = ["start", "resume", "save"]
singleVerb = ["help", "inventory"]

# verbs method ---------------------------------------

# repeats the long form explanation of the room
def lookItem(restOfTheCommand):
	#print restOfTheCommand[0]
	words = restOfTheCommand
	#if preposition provided
	if words[0] == "at":
		item = words[1]
	else:
		item = words[0]
	print "look", item

def goDirection(restOfTheCommand):
	#print restOfTheCommand[0]
	words = restOfTheCommand
	#if preposition provided
	if words[0] == "to":
		item = words[1]
	else:
		item = words[0]
	print "go", item

#acquire an object, putting it into your inventory
def takeItem(item):
	print "take", item

#list a set of verbs the game understands
def helpUser():
	print "following is the list of verbs the game understands:"
	for verb in dispatch:
		print verb
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
def isActionVerb(verb):
	return verb in actionVerb

def isMenuVerb(verb):
	return verb in menuVerb

def isSingleVerb(verb):
	return verb in singleVerb
#--------------------------------------------------------

def commandParsing(userInput):
	#print "this is the input", userInput
	#required verbs and phrases
	verb = userInput.split()[0].lower()
	#check the verb is in the list
	if isActionVerb(verb) or isMenuVerb(verb) or isSingleVerb(verb):
		if isMenuVerb(verb) or isSingleVerb(verb):
			dispatch[verb]()
		else:
			restOfTheCommand = userInput.lower().split()[1:]
			dispatch[verb](restOfTheCommand)
	else:
		print "use 'help' for instruction"
	return

def main():
	command = raw_input("> ")
	commandParsing(command)

if __name__ == "__main__":
    main()
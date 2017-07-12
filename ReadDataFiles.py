'''
Created on Jul 8, 2017

@author: Penny
'''

import json

roomFileNames = ["frontYard.json", "porch.json"]
listOfRooms = {}



def readRoomFiles():
    for i in range(0, len(roomFileNames)):
        with open(roomFileNames[i], 'r') as name:
            listOfRooms.update(json.load(name))
    return listOfRooms
readRoomFiles()
print(listOfRooms["porch"]["west"])

import json
import os

###to-do: figure out what classes and all that do, add in logic, test run###
class npc:
    def __init__(self, name, relationships):
        self.name = name
    if not relationships:
        self.relationships = relationships

    def addRelationship(self, datastore):
        relationship = input()
        relationship = list.append()

    def remRelationship(self, datastore):
        #more logic to remove relationship#

    def addNPC():
    os.popen(file with datastore information)
    username = input("Username")
    relationship = []
   loopRelationship = true
    while loopRelationship:
        relationship.add(input("relationship?"))
        if not relationship:
            looprelationship = false

    def getNPC(name):
    npcs = os.popen(file datastore)
    for npc in npcs:
        if npc["name"] == name:
            print npc["name"]+"\n"
            for relationship in npc["relationships"]:
                print relationship+"\n"


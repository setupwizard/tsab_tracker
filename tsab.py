####################
# Sample script using class & function file
#####################
#Import the npc file from ./functions/npc
from functions import npc
import os
import json

#Instantiate the current npc db
npcsList = npc.getNpcs()
print("Adding new NPC!")


#print the list before you add the new NPC
print("Below is the old NPC list:\r\n",npcsList)
for line in npcsList:
	print(line)

#execute the addNpc function from npc file to add a new NPC
npcsList.add(npc.addNpc())

#print the list after you add the new NPC
print("Below is the new NPC list:\r\n",npcsList)
for npc in npcsList:
	print(npc)
	
#store the npc DB
npc.storeNpcs(npcsList)

print("All done!")

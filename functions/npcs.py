#######################################
#Sample class definitions and functions
#######################################
class npc:
	def __init__(self, name, gender, appearance=[], personalityTraits=[], kin=[], inventory=[]):
		self.name = name
		self.gender = gender
		self.appearance = appearance
		self.personalityTraits = personalityTraits
		self.kin = kin
		self.inventory = inventory
		
	def serialize(self)
		return {
			'name': self.name,
			'gender': self.gender,
			'appearance': self.appearance,
			'traits': self.personalityTraits,
			'kin': self.kin,
			'inventory': self.inventory,
		}
		
	def addPersonalityTrait(self, trait)
		self.personalityTraits.add(trait)
		
	def delPersonalityTrait(self, trait)
		for target in self.personalityTraits:
			if trait["name"] is self.personalityTraits[target]["name"]:
				self.personalityTraits.del(target)
				
	#def add kin/inventory in the same ways as personality traits

def getNpcs():
	parsedNPCs = []
	rawNPC = os.open("./db/npcs","r")
	for npcIter in rawNPC.readline():
		npc = json.loads(npcIter)
		parsedNPCs.add(npc)
	return parsedNPCs
	
def storeNpcs(npcList):
	npcStore = []
	os.remove("./db/npcs")
	npcDb = os.open("./db/npcs","a")
	for npc in npcList:
		jsonifiedNpc = jsonify(npc.serialize())
		npcStore.add(jsonifiedNpc)
	for line in npcStore:
		npcDb.write(line)
	return true

def getAppearances():
	parsedAppearance = []
	rawAppearance = os.open("./db/appearance","r")
	for line in rawAppearance.readlines():
		appearanceParsed = json.dumps(line)
	return parsedAppearance
	
def addNpc():
	cont = true
	name = input("What is the NPCs name?")
	gender = input("What is the NPCs gender?")
	while cont:
		print("Select from the below appearances:")
		for look in getAppearances():
			print(look["name"])
		appearance = input(":")
		if not appearance:
			cont = false
	
	#personalityTraits = just like appearances but with traits db
	#kin = just like appearance but with kin db
	#inventory = just like appearance but with inventory db

import json

def addNonprofit(nonprofitName):
	with open('accounts.json', 'r') as infile:
		data = json.load(infile)
	data["nonprofits"].append({"name": nonprofitName, "accounts": []})
	with open('accounts.json', 'w') as outfile:
		json.dump(data, outfile)

def addAddress(nonprofitName, address):
	with open('accounts.json', 'r') as infile:
		data = json.load(infile)
	index = None
	for i in range(len(data["nonprofits"])):
		if(data["nonprofits"][i]["name"] == nonprofitName):
			index = i
			break
	if(index == None):
		addNonprofit(nonprofitName)
		with open('accounts.json', 'r') as infile:
			data = json.load(infile)
		for i in range(len(data["nonprofits"])):
			if(data["nonprofits"][i]["name"] == nonprofitName):
				index = i
				break
	data["nonprofits"][index]["accounts"].append({"address": address})
	with open('accounts.json', 'w') as outfile:
		json.dump(data, outfile)
	
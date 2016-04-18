import json

def addNonprofit(nonprofitName):
	with open('accounts.json', 'r') as infile:
		data = json.load(infile)
	data["nonprofits"].append({"name": nonprofitName, "accounts": {}})
	with open('accounts.json', 'w') as outfile:
		json.dump(data, outfile)

def addAddress(nonprofitName, address, coin):
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
	if(coin not in data["nonprofits"][index]["accounts"]):
		data["nonprofits"][index]["accounts"][coin] = []
	data["nonprofits"][index]["accounts"][coin].append({"address": address})
	with open('accounts.json', 'w') as outfile:
		json.dump(data, outfile)

def addEtherAddress(nonprofitName, address):
	addAddress(nonprofitName, address, "ETH")
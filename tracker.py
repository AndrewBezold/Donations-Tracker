import requests
import json

def getAmountFromAccountEther(id):
	# loop through transactions of account until field data is empty
	check = False
	iterator = 0
	amount = 0
	while(check == False):
		account = requests.get("https://etherchain.org/api/account/" + id + "/tx/" + str(iterator))
		json_text = json.loads(account.text)
		if(len(json_text["data"]) == 0):
			check = True
		else:
			for i in range(len(json_text["data"])):
				amount += json_text["data"][i]["amount"]
			iterator += 1
	return amount

def getAmountFromMultipleAccountsEther(ids):
	#loop through accounts in ids, adding amount from each
	amount = 0
	for i in range(len(ids)):
		amount += getAmountFromAccountEther(ids[i])
	return amount


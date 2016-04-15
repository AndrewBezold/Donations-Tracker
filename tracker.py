import requests
import json
id = "0xb794f5ea0ba39494ce839613fffba74279579268"
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
print (amount)
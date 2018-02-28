import requests 
from handler import handle_message 
token = "https://api.telegram.org/bot540889680:AAHVdAwR1JxSfJWP61-i0g1eVK-LoK9QfOU/"
last_update = 0
while True:
	temp = dict()
	temp["offset"] = last_update
	req = requests.get(token + "getUpdates", params=temp)
	Inp = req.json()
	print(Inp)

	for el in Inp["result"]:	
		if "message" not in el:
			continue
		else:
			if "text" not in el["message"]:
				continue
		last_update = max(el["update_id"], last_update)
		last_update += 1
		text = el["message"]["text"]
		nick = str(el["message"]["from"]["id"]) + "\n"
		chat_id = el["message"]["from"]["id"]
		ans = handle_message(text, nick)
		requests.post(token + "sendMessage", params={"chat_id": chat_id, "text": "\n".join(ans)})
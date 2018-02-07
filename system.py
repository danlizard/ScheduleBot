import requests 
from handler.py import handle_message 
token = "https://api.telegram.org/bot540889680:AAHVdAwR1JxSfJWP61-i0g1eVK-LoK9QfOU/"

while True:
	req = requests.get(token + "getUpdates")
	Inp = req.json()

	for el in Inp["result"]:
		text = el["message"]["text"]
		nick = el["message"]["from"]["username"]
		chat_id = el["message"]["from"]["id"]
		ans = handle_message(text, nick)

		requests.post(token + "sendMessage", params=("chat_id": chat_id, "text": text))
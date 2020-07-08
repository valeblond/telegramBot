import requests

API_link = "https://api.telegram.org/bot1290187199:AAGEWSR0QXz99jJQNi8F7Wt3vwy1uBrV8X0"


updates = requests.get(API_link + "/getUpdates?offset=-1").json()

print(updates)


message = updates ["result"][0]["message"]

chat_id = message["from"]["id"]
text = message["text"]

sent_message = requests.get(API_link + f"/sendMessage?chat_id={chat_id}&text=Hey man, u wrote {text} motherfucker!!!")



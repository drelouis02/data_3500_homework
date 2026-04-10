import json
import requests

url = "https://api.datamuse.com/words?rel_trg=cow"

req = requests.get(url)
dct1 = json.loads(req.text)

for item in dct1:
    if item.get("word") == "cheese":
        print(item.get("score"))

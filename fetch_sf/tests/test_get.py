import requests
import json

payload = {'order_id':'7890'}
r = requests.get('http://localhost:9977/api/',params=payload)

json_format = json.dumps(r.text,indent=4)

print json_format

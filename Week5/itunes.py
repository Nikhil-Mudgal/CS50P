import sys
import json 
import requests 

if len(sys.argv) != 2:
    sys.exit() # exits the loop 

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term="+sys.argv[1])

# print(json.dumps(response.json(),indent = 2)) # returns a json response and we convert that to a python dict 


o = response.json()

for result in o["results"]:
    print(result["trackName"])
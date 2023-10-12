import requests
import json


token = "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"
username = "samuvack"

url = "https://raw.githubusercontent.com/Informatievlaanderen/data.vlaanderen.be-generated/production/doc/applicatieprofiel/FeitelijkeVerenigingen/context/Feitelijke-Verenigingen-ap.jsonld"

r = requests.get(url, auth=(username, token))
res = r.json()
print(res)

json_object = json.dumps(res, indent=4)

f = open("../oslo/test.jsonld", "w+")
f.write(json_object)
f.close()

import json
import requests

meraki_api_key = '093b24e85df15a3e66f1fc359f4c48493eaa1b73'
mynetwork = 'L_646829496481100388'

url = "https://dashboard.meraki.com/api/v0/networks/"

baseurl = url + mynetwork + "/devices"

payload = {}

header = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": meraki_api_key
}

response = requests.get(baseurl, headers=header, data=payload)
deviceInfo = json.loads(response.text)
print(json.dumps(deviceInfo, sort_keys=True, indent=4))

for item in deviceInfo:
    if "MX" in item["model"]:
        MXcount = MXcount + 1

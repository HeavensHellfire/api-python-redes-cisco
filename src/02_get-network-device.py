import json
import requests
api_url = "http://localhost:58000/api/v1/network-device"

headers={"X-Auth-Token": "NC-6-c2c35b1313be402f95cf-nbi"}

resp = requests.get(api_url, headers=headers)

print("Request status: ", resp.status_code)

response_json = resp.json()
print()
print()
print (response_json)
print()
print()
networkDevices = response_json["response"]

for networkDevice in networkDevices:
    if not networkDevice.get("hostname"):
        print("", "\t", networkDevice["platformId"], "\t", networkDevice["managementIpAddress"])
    else:
        print(networkDevice["hostname"], "\t", networkDevice["platformId"], "\t", networkDevice["managementIpAddress"])

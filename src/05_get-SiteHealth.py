import json
import requests
from tabulate import *

api_url = "http://localhost:58000/api/v1/host"

headers = {
    "X-Auth-Token": "NC-6-c2c35b1313be402f95cf-nbi"
}

resp = requests.get(api_url, headers=headers)

print("Request status: ", resp.status_code)

resp_json = resp.json()


host_list = []

i = 0
for item in resp_json["response"]:
    i += 1

    host_list.append([
        i,
        item["hostName"] if item.get("hostName") else "", 
        item["hostIp"],
        item["connectedInterfaceName"],
        item["vlanId"] if item.get("vlanId") else "",
        item["pingStatus"]
    ])

print(tabulate(host_list, headers=["Hostname","IP","Interfaz", "Vlan", "Status"],tablefmt='rst'))    


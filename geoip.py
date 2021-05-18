import requests
import os
IP = input('Enter The IP you want to lookup:')
url = ("https://freegeoip.app/json/" + IP)
headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

response = requests.request("GET", url, headers=headers)
output = response.json()['ip']
os.system('cls' if os.name=='nt' else 'clear')
print(response.text)
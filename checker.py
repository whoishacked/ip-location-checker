import json
import urllib.request

with open('ip_list.txt', 'r') as infile:
    data = infile.readlines()
    for ip in data:
        ip_list = ip.split()

for ip in ip_list:
    response = urllib.request.urlopen("http://ipwhois.app/json/" + ip)
    geolocation = json.load(response)
    print(f'{geolocation["ip"]} : {geolocation["country"]}')

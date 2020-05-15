import requests

res = requests.get('https://eu.entelicloud.com/enteliweb/api/.bacnet/Benson House/101/analog-input/Present_Value,1?alt=json',auth=('Partner','DemoomeD'),headers={'Content-Type': 'application/json'})

print (res.text)

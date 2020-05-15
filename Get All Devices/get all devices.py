import requests

res = requests.get('https://eu.entelicloud.com/enteliweb/api/.bacnet/Benson House?alt=json',auth=('Partner','DemoomeD'),headers={'Content-Type': 'application/json'})

print (res.text)

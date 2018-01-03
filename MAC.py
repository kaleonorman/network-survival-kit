import pprint
import requests
MAC_URL = 'http://macvendors.co/api/%s'
mac = input('Please input MAC Address: ')
r = requests.get(MAC_URL % mac)

pprint.pprint(r.json())

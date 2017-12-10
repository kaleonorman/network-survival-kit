import pprint
import requests
MAC_URL = 'http://macvendors.co/api/%s'
MAC = input('Please input MAC Address: ')
r = requests.get(MAC_URL % MAC)

pprint.pprint(r.json())
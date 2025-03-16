import urllib.parse
import urllib.request
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

address = "University of the Punjab Lahore"
api_key = "42"  # Include your API key here
url = serviceurl + urllib.parse.urlencode({'address': address, 'key': api_key})
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

print(data)  # Print the data received from the API

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
else:
    place_id = js['results'][0]['place_id']
    print('Place id:', place_id)

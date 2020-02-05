# chapter 13
# using web services

# graded external tool #1
import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
data = urllib.request.urlopen(url, context = ctx).read()
tree = ET.fromstring(data)
counts = tree.findall('comments/comment')

sum = 0
for count in counts:
    ct = int(count.find('count').text)
    sum = sum + ct
print(sum)

# graded external tool #2
import urllib.request, urllib.parse, urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
data = urllib.request.urlopen(url, context = ctx).read()
js = json.loads(data)

sum = 0
for j in js['comments']:
     sum = sum + j['count']
print(sum)

# graded external tool #3
import urllib.request, urllib.parse, urllib.error
import ssl
import json

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    parms = dict()
    parms['address'] = address
    parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    uh = urllib.request.urlopen(url, context = ctx)
    data = uh.read().decode()

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('Failure To Retrieve')
        print(data)
        continue

    place = js['results'][0]['place_id']
    print(place)

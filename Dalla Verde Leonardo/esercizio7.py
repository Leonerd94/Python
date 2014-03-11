# ex 7
import requests
import json
import urllib2

resp = requests.get('http://ialpython.apiary.io/people')
email = resp.json()

name = {}
for k,v in email:
    name[v] = k

print name
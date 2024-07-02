#!/usr/bin/python3
import urllib.request

url = 'https://alx-intranet.hbtn.io' 
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    header_value = response.getheader('X-Request-Id')

print(header_value)


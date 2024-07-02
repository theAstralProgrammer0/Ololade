#!/usr/bin/python3
import urllib.request
import urllib.parse

url = 'http://example.com'
data = urllib.parse.urlencode({'email': 'test@example.com'})
data = data.encode('ascii')  # data should be bytes

req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    print(response.read().decode('utf-8'))


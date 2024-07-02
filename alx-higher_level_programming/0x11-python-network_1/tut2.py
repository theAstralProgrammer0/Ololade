#!/usr/bin/python3
import shutil
import tempfile
import urllib.request

url = 'http://python.org/'

req = urllib.request.Request(url)
print(type(req))

with urllib.request.urlopen(req) as res:
    """data = res.read()"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        shutil.copyfileobj(res, tmp)
"""
print(type(data))
print(data.decode('utf-8'))
"""

with open(tmp.name, mode='r', encoding='utf-8') as tmp_file:
    print(tmp_file.read())


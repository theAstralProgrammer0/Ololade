#!/usr/bin/python3
import shutil
import tempfile
import urllib.request

url = 'http://python.org/'
with urllib.request.urlopen(url) as res:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        shutil.copyfileobj(res, tmp)

with open(tmp.name, mode='r', encoding='utf-8') as html:
    print(type(html))
    print(html.read())

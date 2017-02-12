# -*-coding:utf-8-*-
import requests
import json


#r = requests.get('https://github.com/timeline.json')
payload = {'key1':'value1','key2':'value2'}
r1 = requests.post("http://httpbin.org/post", data=payload)
headers = {'Content-Type':'application/json; charset:UTF-8'}
r2 = requests.post("http://httpbin.org/post", json=payload)
#print r.text
print r1.text
print r2.text
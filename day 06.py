import requests
import pyperclip
from parse import *


jar = requests.cookies.RequestsCookieJar()

jar.set('session', 'secret_key',
        domain='adventofcode.com')

s = requests.Session()
s.cookies = jar
r = s.get('https://adventofcode.com/2019/day/6/input')
response = 0

input_text = r.text

lines = input_text.splitlines()


def check_in_dict(dictionary, key):
    if key not in dictionary:
        dictionary[key] = 0
    return dictionary[key]


def sum_in_dict(dictionary, key, value):
    check_in_dict(dictionary, key)
    dictionary[key] += value

#your code here

orb = {}
orbc = {}
for i in lines:
    a = i.split(')')
    orb[a[1]] = a[0]
"""
for i in orb.keys():
    j = i
    while j in orb.keys():
        sum_in_dict(orbc, i, 1)
        j = orb[j]

for i in orbc.values():
    response += i
"""
orbYou = []
orbSan = []
j = "SAN"
while j in orb.keys():
    orbSan.append(j)
    j = orb[j]
j = "YOU"
while j in orb.keys():
    orbYou.append(j)
    j = orb[j]
for i in orbYou:
    if i in orbSan:
        response = orbYou.index(i)+orbSan.index(i)-2
        break



pyperclip.copy(response)
#not working

#req = requests.Request('POST', "https://adventofcode.com/2018/day/1/answer")
#prepped = req.prepare()

#prepped.body = "level=1&answer="+response

#resp = s.send(prepped)

#print(resp.text)

print(response)
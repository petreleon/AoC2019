import requests
import pyperclip
from parse import *


jar = requests.cookies.RequestsCookieJar()

jar.set('session', 'secret_key',
        domain='adventofcode.com')

s = requests.Session()
s.cookies = jar
r = s.get('https://adventofcode.com/2019/day/3/input')
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


w = lines[0].split(",")
v = [(i[0], int(i[1:])) for i in w]

w = lines[1].split(",")
o = [(i[0], int(i[1:])) for i in w]
dict1 = {}
dict2 = {}

originX = 0
originY = 0

x = originX
y = originY
count_ = 0

for i in v:
    if i[0] == 'U':
        for j in range(i[1]):
            count_ += 1
            y += 1
            sum_in_dict(dict1, (x,y), count_)
    if i[0] == 'D':
        for j in range(i[1]):
            count_ += 1
            y -= 1
            sum_in_dict(dict1, (x,y), count_)
    if i[0] == 'R':
        for j in range(i[1]):
            count_ += 1
            x += 1
            sum_in_dict(dict1, (x,y), count_)
    if i[0] == 'L':
        for j in range(i[1]):
            count_ += 1
            x -= 1
            sum_in_dict(dict1, (x,y), count_)

x = originX
y = originY
count_ = 0

for i in o:

    if i[0] == 'U':
        for j in range(i[1]):
            count_ += 1
            y += 1
            sum_in_dict(dict2, (x,y), count_)
    if i[0] == 'D':
        for j in range(i[1]):
            count_ += 1
            y -= 1
            sum_in_dict(dict2, (x,y), count_)
    if i[0] == 'R':
        for j in range(i[1]):
            count_ += 1
            x += 1
            sum_in_dict(dict2, (x,y), count_)
    if i[0] == 'L':
        for j in range(i[1]):
            count_ += 1
            x -= 1
            sum_in_dict(dict2, (x,y), count_)

interections = [value for value in dict1.keys() if value in dict2.keys()]

interections.sort(key=lambda x: abs(dict1[x])+abs(dict2[x]))

response = abs(dict1[interections[0]])+abs(dict2[interections[0]])

pyperclip.copy(response)
#not working

#req = requests.Request('POST', "https://adventofcode.com/2018/day/1/answer")
#prepped = req.prepare()

#prepped.body = "level=1&answer="+response

#resp = s.send(prepped)

#print(resp.text)

print(response)

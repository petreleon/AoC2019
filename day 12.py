import requests
import pyperclip
import itertools
import math

from parse import *
from copy import *

import math

jar = requests.cookies.RequestsCookieJar()

jar.set('session', 'secret_key',
        domain='adventofcode.com')

s = requests.Session()
s.cookies = jar
r = s.get('https://adventofcode.com/2019/day/12/input')
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


# your code here
'''lines = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>""".splitlines()'''

response = 1
position = []
velocity = [0, 0, 0]
velocities = []

for i in lines:
    a = parse("<x={:d}, y={:d}, z={:d}>", i)
    position.append([a[0], a[1], a[2]])
    velocities.append(copy(velocity))

original_position = deepcopy(position)
original_velocity = deepcopy(velocities)



#for step in range(steps_):
for j in range(len(position[0])):
    steps_ = 0
    while True:
        steps_ += 1
        for i in range(len(position)):

            for k in range(len(position)):
                if position[i][j] > position[k][j]:
                    velocities[i][j] -= 1
                elif position[i][j] < position[k][j]:
                    velocities[i][j] += 1

        for i in range(len(position)):

            position[i][j] += velocities[i][j]

        if position == original_position and velocities == original_velocity:
            response = int(response * steps_ / math.gcd(steps_, response))
            break
        if velocities == original_velocity:
            print("original velocity")
        if position == original_position:
            print("original position")

assert response != 9285608100380604

energy = 0

for i in range(len(position)):
    pot = 0
    cyn = 0
    for j in range(len(position[i])):
        pot += abs(position[i][j])
        cyn += abs(velocities[i][j])
    energy += pot * cyn

#response = energy
pyperclip.copy(response)
# not working

# req = requests.Request('POST', "https://adventofcode.com/2018/day/1/answer")
# prepped = req.prepare()

# prepped.body = "level=1&answer="+response

# resp = s.send(prepped)

# print(resp.text)

print(response)

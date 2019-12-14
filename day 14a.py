import requests
import pyperclip
import itertools
import functools
import math
import random
from fractions import Fraction

from parse import *
from copy import *

import math

jar = requests.cookies.RequestsCookieJar()

jar.set('session', 'secret_key',
        domain='adventofcode.com')

s = requests.Session()
s.cookies = jar
r = s.get('https://adventofcode.com/2019/day/14/input')
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
# lines[0]='3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'

"""lines = '''9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL'''.splitlines()"""

chemical_reactions = {}


class Element:
    def __init__(self, quantity, list_):
        self.quantity = quantity
        self.list_ = deepcopy(list_)
        self.level = 0


for line in lines:
    [combine, result] = line.split(' => ')
    combine = combine.split(', ')
    for i in range(len(combine)):
        struct = parse('{:d} {}', combine[i])
        combine[i] = (struct[0], struct[1])
    struct = parse('{:d} {}', result)
    result = (struct[0], struct[1])
    chemical_reactions[result[1]] = Element(result[0], combine)

maxLevel = 0


def recursiveAsign(e: Element, i: int):
    global maxLevel
    global chemical_reactions
    maxLevel = max(maxLevel, i)
    if e.level < i:
        e.level = i
    for j in e.list_:
        if j[1] in chemical_reactions.keys():
            recursiveAsign(chemical_reactions[j[1]], i+1)

recursiveAsign(chemical_reactions['FUEL'], 0)

list_of_reaction = deepcopy(chemical_reactions['FUEL'].list_)

lambda_ = lambda x: (chemical_reactions[x[1]].level, x[1]) if x[1] in chemical_reactions.keys() else (maxLevel+1, x[1])
list_of_reaction.sort(key=lambda_)

while list_of_reaction[0][1] != 'ORE':
    i = 0
    un_divisible_quantity = chemical_reactions[list_of_reaction[0][1]].quantity
    quantity = (list_of_reaction[0][0]+un_divisible_quantity-1)//un_divisible_quantity
    list_of_reaction[0:1] = list(map(lambda x: (x[0]*quantity, x[1]), chemical_reactions[list_of_reaction[0][1]].list_))
    list_of_reaction.sort(key=lambda_)
    while i < len(list_of_reaction) - 1:
        if list_of_reaction[i][1] == list_of_reaction[i + 1][1]:
            list_of_reaction[i:i+2] = [(list_of_reaction[i][0]+list_of_reaction[i+1][0], list_of_reaction[i][1])]
        else:
            i += 1

response = list_of_reaction[0][0]

pyperclip.copy(response)
# not working

# req = requests.Request('POST', "https://adventofcode.com/2018/day/1/answer")
# prepped = req.prepare()

# prepped.body = "level=1&answer="+response

# resp = s.send(prepped)

# print(resp.text)

print(response)

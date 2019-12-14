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

"""lines = '''171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX'''.splitlines()"""

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


def fuel_to_ore(number):
    global chemical_reactions
    list_of_reaction = [(number, "FUEL")]
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
    return list_of_reaction[0][0]

max_number = 1000000000000
i = 1

while fuel_to_ore(i) < max_number:
    i *= 10

pair_of_numbers = (i//10, i)

while abs(pair_of_numbers[1] - pair_of_numbers[0])>10:
    number_to_test = (pair_of_numbers[1]+pair_of_numbers[0])//2
    if fuel_to_ore(number_to_test)<=max_number:
        pair_of_numbers = (number_to_test ,pair_of_numbers[1])
    else:
        pair_of_numbers = (pair_of_numbers[0], number_to_test)

for i in range(pair_of_numbers[0], pair_of_numbers[1]+1):
    x = fuel_to_ore(i)
    if x < max_number:
        response = i


pyperclip.copy(response)
# not working

# req = requests.Request('POST', "https://adventofcode.com/2018/day/1/answer")
# prepped = req.prepare()

# prepped.body = "level=1&answer="+response

# resp = s.send(prepped)

# print(resp.text)

print(response)

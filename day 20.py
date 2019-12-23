import requests
import pyperclip
import itertools
import functools
import math
import random
from fractions import Fraction
from intcode import *
import sys
from itertools import permutations

from parse import *
from copy import *

import math

jar = requests.cookies.RequestsCookieJar()

jar.set('session', 'secret',
        domain='adventofcode.com')

s = requests.Session()
s.cookies = jar
r = s.get('https://adventofcode.com/2019/day/21/input')
response = 0

input_text = r.text

lines = input_text.splitlines()

list_ = list(map(int, lines[0].split(',')))
list_.extend([0]*10000)

stringToInput = ''

'''
FIRST INPUT:

OR A T
AND B T
AND C T
NOT D J
OR J T
NOT T J
WALK
'''
'''
// not working
SECOND INPUT:

FIRST ATTEMPT
OR A T
AND B T
AND C T
NOT D J
OR J T
NOT T J
OR D T
AND I T
OR H T
AND T J
NOT A T
OR T J
RUN

SECOND ATTEMPT
OR A T
AND B T
AND C T
NOT T J
AND D J
AND E J
AND F J
RUN

THIRD ATTEMPT

OR A J
AND E J

Final:
NOT F J
OR E J
OR H J
AND D J
NOT C T
AND T J
NOT D T
OR B T
OR E T
NOT T T
OR T J
NOT A T
OR T J
RUN

'''

indexOfInput = 0

def input_():
    global stringToInput
    global indexOfInput
    indexOfInput += 1
    if indexOfInput >= len(stringToInput):
        stringToInput = input()+'\n'
        indexOfInput = 0

    return ord(stringToInput[indexOfInput])


def print_(val):
    global response
    if val > 256:
        print(val)
    else:
        print(chr(val), end='')


machine(input_, print_, list_)

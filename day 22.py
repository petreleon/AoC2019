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
r = s.get('https://adventofcode.com/2019/day/22/input')
response = 0

input_text = r.text

lines = input_text.splitlines()

'''list_ = list(map(int, lines[0].split(',')))
list_.extend([0]*10000)
'''
'''
#first solution
stack = list(range(10007))

for line in lines:
    if 'deal into new stack' in line:
        stack.reverse()
    if 'cut' in line:
        number = parse("cut {:d}", line)[0]
        if number < 0:
            number += len(stack)
        temp_list = stack[0:number]
        stack[0:number] = []
        stack.extend(temp_list)
    if 'deal with increment' in line:
        number = parse("deal with increment {:d}", line)[0]
        temp_list = copy(stack)
        for i in range(len(stack)):
            temp_list[(i * number)%len(temp_list)] = stack[i]
        stack = temp_list

response = stack.index(2019)'''

lenOfRange = 119315717514047
pos2020 = 2020

lines.reverse()


def modInverse(a, m):
    g = gcd(a, m)

    if (g != 1):
        print("Inverse doesn't exist")

    else:

        # If a and m are relatively prime,
        # then modulo inverse is a^(m-2) mode m
        print("Modular multiplicative inverse is ",
              power(a, m - 2, m))

    # To compute x^y under modulo m


def power(x, y, m):
    if (y == 0):
        return 1

    p = power(x, y // 2, m) % m
    p = (p * p) % m

    if (y % 2 == 0):
        return p
    else:
        return ((x * p) % m)

    # Function to return gcd of a and b


def gcd(a, b):
    if (a == 0):
        return b

    return gcd(b % a, a)




for line in lines:
    if 'deal into new stack' in line:
        pos2020 = lenOfRange - pos2020 - 1
    if 'cut' in line:
        number = parse("cut {:d}", line)[0]
        if number < 0:
            number += lenOfRange
        number = lenOfRange - number
        if pos2020 < number:
            pos2020 += lenOfRange - number
        else:
            pos2020 -= number
    if 'deal with increment' in line:
        number = parse("deal with increment {:d}", line)[0]
        '''c = 0
        while (c*number)%lenOfRange != pos2020:
            c += 1'''
        print('increment is '+str(number)+', and pos2020 is '+str(pos2020))
        pos2020 = int(input("enter new pos2020"))

response = pos2020
#assert response > 27971594186726
print(response)


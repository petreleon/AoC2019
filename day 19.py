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

sys.setrecursionlimit(15000)

from parse import *
from copy import *

import math

jar = requests.cookies.RequestsCookieJar()

jar.set('session', 'secretkey',
        domain='adventofcode.com')

s = requests.Session()
s.cookies = jar
r = s.get('https://adventofcode.com/2019/day/19/input')
response = 0

input_text = r.text

lines = input_text.splitlines()


def check_in_dict(dictionary, key, default=0):
    if key not in dictionary:
        dictionary[key] = 0
    return dictionary[key]


def sum_in_dict(dictionary, key, value, default=0):
    check_in_dict(dictionary, key, default)
    dictionary[key] += value


def append_in_dict_of_sets(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = set()
    dictionary[key].add(value)


def append_in_dict_of_lists(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = []
    dictionary[key].append(value)


def extend_in_dict_of_lists(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = []
    dictionary[key].extend(value)


# your code here

#squares = range



def input_():
    global input_list
    global input_index
    input_index += 1
    return input_list[input_index - 1]

fitting = 0
def check_fitting(i):
    global fitting
    fitting = i

'''list_ = list(map(int, lines[0].split(',')))
list_.extend([0]*10000)'''

def checking(i, j):
    global input_list
    global input_index
    global fitting
    list_ = list(map(int, lines[0].split(',')))
    list_.extend([0] * 10000)
    input_list = [i, j]
    input_index = 0
    machine(input_, check_fitting, list_)
    if fitting == 0:
        return False
    return True


response_found = False
initial_x = 100
initial_y = 100

while not response_found:
    response_found = True
    while not checking(initial_x, initial_y + 99):
        response_found = False
        initial_x += 1
    while not checking(initial_x + 99, initial_y):
        response_found = False
        initial_y += 1


response = 10000 * initial_x + initial_y

assert response < 17462084

print(checking(0, 3))
pyperclip.copy(response)

print(response)
'''        for j in range(initial_x, initial_x + 100):
            if not checking(j, i):
                initial_y += 1
                to_break = True
                response_found = False
                break'''

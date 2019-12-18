import requests
import pyperclip
import itertools
import functools
import math
import random
from fractions import Fraction
from intcode import *

from parse import *
from copy import *

import math

jar = requests.cookies.RequestsCookieJar()

jar.set('session', 'secret_key',
        domain='adventofcode.com')

s = requests.Session()
s.cookies = jar
r = s.get('https://adventofcode.com/2019/day/17/input')
response = 0

input_text = r.text

lines = input_text.splitlines()


def check_in_dict(dictionary, key, default=0):
    if key not in dictionary:
        dictionary[key] = 0
    return dictionary[key]


def sum_in_dict(dictionary, key, value, default= 0):
    check_in_dict(dictionary, key, default)
    dictionary[key] += value




# your code here
#lines[0] = '12345678'


list_ = list(map(int, lines[0].split(',')))
list_.extend([0]*100000)
list_[0] = 2

chars = ""
init = False

listOfInputs = ''
inputIndex = 0

def output(a):
    global chars
    print(a)
    chars += str(chr(a))


def forward(actual_position, direction):
    assert 0 <= direction < 4
    if direction == 0:
        forward_position = (actual_position[0], actual_position[1] + 1)
    elif direction == 1:
        forward_position = (actual_position[0] + 1, actual_position[1])
    elif direction == 2:
        forward_position = (actual_position[0], actual_position[1] - 1)
    else:
        # direction == 3
        forward_position = (actual_position[0] - 1, actual_position[1])
    return forward_position


def left(actual_position, direction):
    return forward(actual_position, (direction-1) % 4)


def right(actual_position, direction):
    return forward(actual_position, (direction+1) % 4)

def move_possible(future_position, map_):
    if map_[future_position[0]][future_position[1]] == '#':
        return True
    return False


def rotate_right(direction):
    return (direction + 1) % 4


def rotate_left(direction):
    return (direction - 1) % 4

'''def verifier(entireSequenqe, repeats, actualPosition):
    if actualPosition not in repeats.keys():
        return []
    a = []
    for i in repeats[actualPosition]:
'''


def input_():
    global chars
    global init
    global listOfInputs
    global inputIndex
    print(chars)
    if not init:
        init = True
        table = chars.splitlines()[:-2]
        for i in range(len(table)):
            table[i] = '.'+table[i]+'.'
        emptyLine = '.' * len(table[0])
        table.insert(0, emptyLine)
        table.append(emptyLine)
        actualPosition = (21, 13)
        direction = 3
        list_of_instructions = []
        while move_possible(forward(actualPosition, direction), table) or move_possible(left(actualPosition, direction), table) or move_possible(right(actualPosition, direction), table):
            if move_possible(forward(actualPosition, direction), table):
                list_of_instructions[-1] = (list_of_instructions[-1][0], list_of_instructions[-1][1]+1)
            else:
                if move_possible(left(actualPosition, direction), table):
                    direction = rotate_left(direction)
                    list_of_instructions.append(('L', 1))
                if move_possible(right(actualPosition, direction), table):
                    direction = rotate_right(direction)
                    list_of_instructions.append(('R', 1))
            actualPosition = forward(actualPosition, direction)
        A = 'L,12,L,12,L,6,L,6\n'
        B = 'R,8,R,4,L,12\n'
        C = 'L,12,L,6,R,12,R,8\n'
        seq = 'A,B,A,C,B,A,C,B,A,C\n'
        listOfInputs = seq + A + B + C + 'n\n'
    chars = ""
    char = listOfInputs[inputIndex]
    inputIndex+=1

    return ord(char)

machine(input_, output, list_)

print(chars)

chars = chars.splitlines()
'''
del(chars[-1])

for i in range(1, len(chars)-1):
    for j in range(1, len(chars[i])-1):

        if chars[i][j] == '#' and chars[i+1][j] == '#' and chars[i-1][j] == '#' and chars[i][j+1] == '#' and chars[i][j-1] == '#':
            print((i, j))
            response += i*j
'''
pyperclip.copy(response)
# not working

# req = requests.Request('POST', "https://adventofcode.com/2018/day/1/answer")
# prepped = req.prepare()

# prepped.body = "level=1&answer="+response

# resp = s.send(prepped)

# print(resp.text)


print(response)

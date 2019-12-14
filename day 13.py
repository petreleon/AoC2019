import requests
import pyperclip
import itertools
import functools
import math
import random

from parse import *
from copy import *

import math

jar = requests.cookies.RequestsCookieJar()

jar.set('session', 'secret_key',
        domain='adventofcode.com')

s = requests.Session()
s.cookies = jar
r = s.get('https://adventofcode.com/2019/day/13/input')
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

def param_mode(instruction, index_of_param):
    return instruction // (100 * 10 ** index_of_param) % 10


def position(list_, mode, relative_index, location):
    if mode == 0:
        return list_[location]
    if mode == 1:
        return location
    if mode == 2:
        return list_[location] + relative_index


def machine(input_, output_, list_, position_index=0):
    relative = 0
    compute_index = position_index

    while list_[compute_index] % 100 != 99:
        opcode = list_[compute_index] % 100
        before_change = list_[compute_index]

        (first_param, second_param, third_param) = tuple(map(lambda param_index:
                                                             position(list_,
                                                                      param_mode(list_[compute_index],
                                                                                 param_index),
                                                                      relative,
                                                                      compute_index + 1 + param_index),
                                                             range(3)))
        if opcode == 5:
            if list_[first_param]:
                compute_index = list_[second_param]
            else:
                compute_index += 3

        if opcode == 6:
            if not list_[first_param]:
                compute_index = list_[second_param]
            else:
                compute_index += 3

        if opcode == 1:
            list_[third_param] = list_[first_param] + list_[second_param]
            # i+=4
            if third_param != compute_index:
                compute_index += 4
        if opcode == 2:
            list_[third_param] = list_[first_param] * list_[second_param]
            # i+=4
            if third_param != compute_index:
                compute_index += 4
        if opcode == 3:
            list_[first_param] = int(input_())

            compute_index += 2
        if opcode == 4:
            output_(list_[first_param])
            compute_index += 2
            #return compute_index

        if opcode == 7:
            if list_[first_param] < list_[second_param]:
                list_[third_param] = 1
            else:
                list_[third_param] = 0
            # i+=4
            if third_param != compute_index:
                compute_index += 4

        if opcode == 8:
            if list_[first_param] == list_[second_param]:
                list_[third_param] = 1
            else:
                list_[third_param] = 0
            # i+=4
            if third_param != compute_index:
                compute_index += 4

        if opcode == 9:
            relative += list_[first_param]
            compute_index += 2

    return compute_index


dict_ = {}
coordinates = []
actual_coordinates = []
pad_x_coordinate = 0
'''def print_(value):
    global coordinates
    global dict_
    coordinates.append(value)
    if len(coordinates) == 3:
        dict_[(coordinates[0], coordinates[1])] = value
        coordinates.clear()
'''


def print_blocks(value):
    global coordinates
    global dict_
    coordinates.append(value)
    if len(coordinates) == 3:
        dict_[(coordinates[0], coordinates[1])] = value
        coordinates.clear()


max_x_coordinate = 40
max_y_coordinate = 26

ball_direction = (1, 1)
ball_coordinates = (0, 0)
paddle_coordinates = (0,0)

line = [' ']*(max_x_coordinate+1)
display = []
for i in range(max_y_coordinate+1):
    display.append(copy(line))


def print_(value):
    global max_x_coordinate
    global max_y_coordinate
    global coordinates
    global dict_
    global response
    global actual_coordinates
    global dict_display
    global testable_input
    global good_input
    global display
    global ball_coordinates
    global paddle_coordinates
    coordinates.append(value)
    if len(coordinates) == 3:
        if coordinates[0] == -1 and coordinates[1] == 0:


            #actual_coordinates.clear()
            response = coordinates[2]
            print(testable_input)
            print(response)
        else:
            if coordinates[0]>max_x_coordinate:
                max_x_coordinate = coordinates[0]
            if coordinates[1]>max_y_coordinate:
                max_y_coordinate = coordinates[1]
            actual_coordinates.append((coordinates[0], coordinates[1], coordinates[2]))
        coordinates.clear()



#good_input = [-1, 0, 1, 1, 1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1]
good_input = [1, 0, 0, 0, 1, 1, 1, 0, 0, 0]
testable_input = []
input_iterator = 0


def input_():
    global input_iterator
    global good_input
    global testable_input
    global display
    global actual_coordinates
    global ball_coordinates
    global paddle_coordinates
    for i in actual_coordinates:
        display[i[1]][i[0]] = dict_display[i[2]]
        if display[i[1]][i[0]] == '©':
            ball_coordinates = (i[0], i[1])
        if display[i[1]][i[0]] == 'P':
            paddle_coordinates = (i[0], i[1])
    actual_coordinates.clear()
    for j in display:
        print(''.join(j))
    if paddle_coordinates[0] < ball_coordinates[0]:
        resp = 1
    if paddle_coordinates[0] > ball_coordinates[0]:
        resp = -1
    if paddle_coordinates[0] == ball_coordinates[0]:
        resp = 0
    resp = int(input())
    return resp


list_ = list(map(int, lines[0].split(',')))
list_.extend([0] * 50000)
list_2 = list_.copy()
list_[0] = 2
machine(input, print_blocks, list_2)

dict_display = {
    0: ' ',
    1: 'W',
    2: '+',
    3: 'P',
    4: '©'
}






machine(input_, print_, list_)


'''
actual_coordinates.sort(key=lambda x: -x[2])
for i in actual_coordinates:
response += i[2]
    '''
'''
for i in dict_.values():
    if i == 2:
        response += 1
'''

print(response)

assert response != 1060
assert response != 1056
assert response > 432


pyperclip.copy(response)
# not working

# req = requests.Request('POST', "https://adventofcode.com/2018/day/1/answer")
# prepped = req.prepare()

# prepped.body = "level=1&answer="+response

# resp = s.send(prepped)

# print(resp.text)

print(response)

import requests
import pyperclip
import itertools
import math

from parse import *

import math

jar = requests.cookies.RequestsCookieJar()

jar.set('session', 'secret_key',
        domain='adventofcode.com')

s = requests.Session()
s.cookies = jar
r = s.get('https://adventofcode.com/2019/day/10/input')
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
'''
lines = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##""".splitlines()
'''

def equation(x, point1, point2):
    x1 = point1[0]
    x2 = point2[0]
    y1 = point1[1]
    y2 = point2[1]
    return (x - x1) * (y2 - y1) / (x2 - x1) + y1


def obstacle_check(lines, point1, point2):
    obstacle = False
    if point1[0] == point2[0]:
        if point1[1] > point2[1]:
            (point1, point2) = (point2, point1)
        for i in range(point1[1] + 1, point2[1]):
            if lines[i][point1[0]] == '#':
                obstacle = True
                break
    else:
        if point1[0] > point2[0]:
            (point1, point2) = (point2, point1)
        for i in range(point1[0] + 1, point2[0]):
            y = equation(i, point1, point2)
            if y % 1 == 0:
                y = int(y)
                if lines[y][i] == '#':
                    obstacle = True
                    break
    return obstacle


total_cells = len(lines) * len(lines[0])
width = len(lines[0])
points = {}

for i in range(total_cells):
    if lines[i // width][i % width] == '#':
        for j in range(i+1, total_cells):
            if lines[j // width][j % width] == '#':
                (point1, point2) = ((i % width, i // width), (j % width, j // width))
                if not obstacle_check(lines, point1, point2):
                    sum_in_dict(points, point1, 1)
                    sum_in_dict(points, point2, 1)

key_list = list(points.keys())
val_list = list(points.values())

response = max(points.values())
dict_of_lists = {}

best_point = key_list[val_list.index(response)]
for j in range(len(lines)):
    for i in range(len(lines[0])):
        if (i, j) != best_point and lines[j][i] == '#':
            val_key = math.atan2(i-best_point[0], best_point[1]-j)  #to work here
            if val_key < 0:
                val_key += math.pi * 2
            if val_key not in dict_of_lists:
                dict_of_lists[val_key] = []
            dict_of_lists[val_key].append((i, j))

print(best_point)
for a in dict_of_lists.values():
    a.sort(key=lambda x: abs(x[0] - best_point[0])+abs(x[1]-best_point[1]))

a = list(map(lambda x: [math.degrees(x), dict_of_lists[x]], list(dict_of_lists.keys())))
a.sort()
print(a)

list_of_asteroids = []

to_continue = True
while to_continue:
    to_continue = False
    for i in range(len(a)):
        if len(a[i][1]) > 0:
            to_continue = True
            list_of_asteroids.append(a[i][1][0])
            a[i][1] = a[i][1][1:]

the200th = list_of_asteroids[199]
response = the200th[0]*100 + the200th[1]
pyperclip.copy(response)
# not working

# req = requests.Request('POST', "https://adventofcode.com/2018/day/1/answer")
# prepped = req.prepare()

# prepped.body = "level=1&answer="+response

# resp = s.send(prepped)

# print(resp.text)

print(response)

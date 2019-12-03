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


splited_line = lines[0].split(",")
line1_commands = [(i[0], int(i[1:])) for i in splited_line]

splited_line = lines[1].split(",")
line2_commands = [(i[0], int(i[1:])) for i in splited_line]
line1_steps = {}
line2_steps = {}

originX = 0
originY = 0

actualLineX = originX
actualLineY = originY
count_steps = 0

for actual_command in line1_commands:
    if actual_command[0] == 'U':
        for repeating_iterator in range(actual_command[1]):
            count_steps += 1
            actualLineY += 1
            sum_in_dict(line1_steps, (actualLineX, actualLineY), count_steps)
    if actual_command[0] == 'D':
        for repeating_iterator in range(actual_command[1]):
            count_steps += 1
            actualLineY -= 1
            sum_in_dict(line1_steps, (actualLineX, actualLineY), count_steps)
    if actual_command[0] == 'R':
        for repeating_iterator in range(actual_command[1]):
            count_steps += 1
            actualLineX += 1
            sum_in_dict(line1_steps, (actualLineX, actualLineY), count_steps)
    if actual_command[0] == 'L':
        for repeating_iterator in range(actual_command[1]):
            count_steps += 1
            actualLineX -= 1
            sum_in_dict(line1_steps, (actualLineX, actualLineY), count_steps)

actualLineX = originX
actualLineY = originY
count_steps = 0

for actual_command in line2_commands:

    if actual_command[0] == 'U':
        for repeating_iterator in range(actual_command[1]):
            count_steps += 1
            actualLineY += 1
            sum_in_dict(line2_steps, (actualLineX, actualLineY), count_steps)
    if actual_command[0] == 'D':
        for repeating_iterator in range(actual_command[1]):
            count_steps += 1
            actualLineY -= 1
            sum_in_dict(line2_steps, (actualLineX, actualLineY), count_steps)
    if actual_command[0] == 'R':
        for repeating_iterator in range(actual_command[1]):
            count_steps += 1
            actualLineX += 1
            sum_in_dict(line2_steps, (actualLineX, actualLineY), count_steps)
    if actual_command[0] == 'L':
        for repeating_iterator in range(actual_command[1]):
            count_steps += 1
            actualLineX -= 1
            sum_in_dict(line2_steps, (actualLineX, actualLineY), count_steps)

interections = [value for value in line1_steps.keys() if value in line2_steps.keys()]

interections.sort(key=lambda x: abs(line1_steps[x]) + abs(line2_steps[x]))

response = abs(line1_steps[interections[0]]) + abs(line2_steps[interections[0]])

pyperclip.copy(response)
#not working

#req = requests.Request('POST', "https://adventofcode.com/2018/day/1/answer")
#prepped = req.prepare()

#prepped.body = "level=1&answer="+response

#resp = s.send(prepped)

#print(resp.text)

print(response)

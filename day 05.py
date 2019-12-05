import requests
import pyperclip
from parse import *


jar = requests.cookies.RequestsCookieJar()

jar.set('session', 'secret_key',
        domain='adventofcode.com')

s = requests.Session()
s.cookies = jar
r = s.get('https://adventofcode.com/2019/day/5/input')
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

response = 0

list_ = list(map(int, lines[0].split(',')))
i = 0

while list_[i]%100!=99:
    opcode = list_[i]%100
    before_change = list_[i]
    first_param_mode = (list_[i]//100)%10
    second_param_mode = (list_[i]//1000)%10
    third_param_mode = (list_[i]//10000)%10
    if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:

        if first_param_mode == 0:
            first_param = list_[i+1]
        else:
            first_param = i + 1

        if second_param_mode == 0:
            second_param = list_[i + 2]
        else:
            second_param = i + 2

        if third_param_mode == 0:
            third_param = list_[i+3]
        else:
            third_param = i + 3

    if opcode == 5 or opcode == 6:
        if first_param_mode == 0:
            first_param = list_[i+1]
        else:
            first_param = i + 1

        if second_param_mode == 0:
            second_param = list_[i + 2]
        else:
            second_param = i + 2

    if opcode == 5:
        if list_[first_param]:
            i = list_[second_param]
        else:
            i += 3

    if opcode == 6:
        if not list_[first_param]:
            i = list_[second_param]
        else:
            i += 3

    if opcode == 1:
        list_[third_param] = list_[first_param] + list_[second_param]
        if third_param != i:
            i += 4
    if opcode == 2:
        list_[third_param] = list_[first_param] * list_[second_param]
        if third_param != i:
            i += 4
    if opcode == 3:
        input_ = int(input())
        list_[list_[i+1]] = input_
        i += 2
    if opcode == 4:
        print(list_[list_[i + 1]])
        i += 2

    if opcode == 7:
        if list_[first_param] < list_[second_param]:
            list_[third_param] = 1
        else:
            list_[third_param] = 0

        if third_param != i:
            i += 4

    if opcode == 8:
        if list_[first_param] == list_[second_param]:
            list_[third_param] = 1
        else:
            list_[third_param] = 0

        if third_param != i:
            i += 4






pyperclip.copy(response)
#not working

#req = requests.Request('POST', "https://adventofcode.com/2018/day/1/answer")
#prepped = req.prepare()

#prepped.body = "level=1&answer="+response

#resp = s.send(prepped)

#print(resp.text)

print(response)
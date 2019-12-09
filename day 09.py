import requests
import pyperclip
import itertools

from parse import *


jar = requests.cookies.RequestsCookieJar()

jar.set('session', 'secret_key',
        domain='adventofcode.com')

s = requests.Session()
s.cookies = jar
r = s.get('https://adventofcode.com/2019/day/9/input')
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

# lines[0]='3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'


def machine():
    relative = 0
    global lines
    list_ = list(map(int, lines[0].split(',')))
    list_.extend([0]*50000)
    i = 0

    while list_[i]%100!=99:
        opcode = list_[i]%100
        before_change = list_[i]
        first_param_mode = (list_[i]//100)%10
        second_param_mode = (list_[i]//1000)%10
        third_param_mode = (list_[i]//10000)%10

        if first_param_mode == 0:
            first_param = list_[i+1]
        elif first_param_mode == 1:
            first_param = i + 1
        else:
            first_param = list_[i + 1] + relative

        if second_param_mode == 0:
            second_param = list_[i + 2]
        elif second_param_mode == 1:
            second_param = i + 2
        else:
            second_param = list_[i + 2] + relative

        if third_param_mode == 0:
            third_param = list_[i+3]
        elif third_param_mode == 1:
            third_param = i + 3
        else:
            third_param = list_[i + 3] + relative


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
            #i+=4
            if third_param != i:
                i += 4
        if opcode == 2:
            list_[third_param] = list_[first_param] * list_[second_param]
            #i+=4
            if third_param != i:
                i += 4
        if opcode == 3:
            list_[first_param] = int(input())

            i += 2
        if opcode == 4:
            print(list_[first_param])
            i += 2

        if opcode == 7:
            if list_[first_param] < list_[second_param]:
                list_[third_param] = 1
            else:
                list_[third_param] = 0
            #i+=4
            if third_param != i:
                i += 4

        if opcode == 8:
            if list_[first_param] == list_[second_param]:
                list_[third_param] = 1
            else:
                list_[third_param] = 0
            #i+=4
            if third_param != i:
                i += 4

        if opcode == 9:
            relative += list_[first_param]
            i+=2

    #return response


w = list(itertools.permutations([5, 6, 7, 8, 9]))
max_ = 0
"""for i in w:
    input_ = 0
    amplifiers = []
    for j in i:
        amplifiers.append(Amplifier(j))
    k = 0
    while amplifiers[0].end != True:
        amplifiers[k].machine(input_)
        input_ = amplifiers[k].response
        k = (k+1) % len(i)
    if amplifiers[-1].response > max_:
        max_ = amplifiers[-1].response


response = max_

"""
machine()
pyperclip.copy(response)
#not working

#req = requests.Request('POST', "https://adventofcode.com/2018/day/1/answer")
#prepped = req.prepare()

#prepped.body = "level=1&answer="+response

#resp = s.send(prepped)

#print(resp.text)

print(response)
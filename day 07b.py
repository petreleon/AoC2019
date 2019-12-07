import requests
import pyperclip
import itertools

from parse import *


jar = requests.cookies.RequestsCookieJar()

jar.set('session', 'secret_key',
        domain='adventofcode.com')

s = requests.Session()
s.cookies = jar
r = s.get('https://adventofcode.com/2019/day/7/input')
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


class Amplifier:
    def __init__(self, phaseParam):
        global lines
        self.phaseParam = phaseParam
        #self.inputParam = inputParam
        self.response = 0
        self.phaseParamTaken = False
        self.list_ = list(map(int, lines[0].split(',')))
        self.i = 0
        self.end = False

    def machine(self, input_param):
        response = -1
        if self.list_[self.i] % 100 == 99:
            self.end = True
        while self.list_[self.i] % 100 != 99:
            self.opcode = self.list_[self.i] % 100
            self.before_change = self.list_[self.i]
            self.first_param_mode = (self.list_[self.i] // 100) % 10
            self.second_param_mode = (self.list_[self.i] // 1000) % 10
            self.third_param_mode = (self.list_[self.i] // 10000) % 10
            if self.opcode == 1 or self.opcode == 2 or self.opcode == 7 or self.opcode == 8:

                if self.first_param_mode == 0:
                    self.first_param = self.list_[self.i + 1]
                else:
                    self.first_param = self.i + 1

                if self.second_param_mode == 0:
                    self.second_param = self.list_[self.i + 2]
                else:
                    self.second_param = self.i + 2

                if self.third_param_mode == 0:
                    self.third_param = self.list_[self.i + 3]
                else:
                    self.third_param = self.i + 3

            if self.opcode == 5 or self.opcode == 6:
                if self.first_param_mode == 0:
                    self.first_param = self.list_[self.i + 1]
                else:
                    self.first_param = self.i + 1

                if self.second_param_mode == 0:
                    self.second_param = self.list_[self.i + 2]
                else:
                    self.second_param = self.i + 2

            if self.opcode == 5:
                if self.list_[self.first_param]:
                    self.i = self.list_[self.second_param]
                else:
                    self.i += 3

            if self.opcode == 6:
                if not self.list_[self.first_param]:
                    self.i = self.list_[self.second_param]
                else:
                    self.i += 3

            if self.opcode == 1:
                self.list_[self.third_param] = self.list_[self.first_param] + self.list_[self.second_param]
                if self.third_param != self.i:
                    self.i += 4
            if self.opcode == 2:
                self.list_[self.third_param] = self.list_[self.first_param] * self.list_[self.second_param]
                if self.third_param != self.i:
                    self.i += 4
            if self.opcode == 3:
                if self.phaseParamTaken:
                    self.list_[self.list_[self.i + 1]] = input_param
                    self.i += 2
                else:
                    self.list_[self.list_[self.i + 1]] = self.phaseParam
                    self.phaseParamTaken = True
                    self.i += 2
            if self.opcode == 4:
                # inputParam = self.list_[self.list_[self.i + 1]]
                self.response = self.list_[self.list_[self.i + 1]]
                self.i += 2
                return self.response

            if self.opcode == 7:
                if self.list_[self.first_param] < self.list_[self.second_param]:
                    self.list_[self.third_param] = 1
                else:
                    self.list_[self.third_param] = 0

                if self.third_param != self.i:
                    self.i += 4

            if self.opcode == 8:
                if self.list_[self.first_param] == self.list_[self.second_param]:
                    self.list_[self.third_param] = 1
                else:
                    self.list_[self.third_param] = 0

                if self.third_param != self.i:
                    self.i += 4
        return response


def machine(phaseParam, inputParam):
    response = 0
    phaseParamTaken = False
    global lines
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
            if phaseParamTaken:
                list_[list_[i+1]] = inputParam
            else:
                list_[list_[i+1]] = phaseParam
                phaseParamTaken = True
            i += 2
        if opcode == 4:
            inputParam = list_[list_[i + 1]]
            response = list_[list_[i + 1]]
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

    return response


w = list(itertools.permutations([5, 6, 7, 8, 9]))
max_ = 0
for i in w:
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


pyperclip.copy(response)
#not working

#req = requests.Request('POST', "https://adventofcode.com/2018/day/1/answer")
#prepped = req.prepare()

#prepped.body = "level=1&answer="+response

#resp = s.send(prepped)

#print(resp.text)

print(response)
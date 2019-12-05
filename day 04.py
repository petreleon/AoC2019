import requests
import pyperclip
from parse import *


jar = requests.cookies.RequestsCookieJar()

jar.set('session', 'secret_key',
        domain='adventofcode.com')

s = requests.Session()
s.cookies = jar
r = s.get('https://adventofcode.com/2019/day/4/input')
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

min_max = list(map(int, lines[0].split('-')))

min_ = min_max[0]
max_ = min_max[1]


for trying_number in range(min_, max_):
    temp = trying_number
    isRepeating = False
    isIncreasing = True
    lastDigit = 10
    while temp>0:
        if temp != 0 and temp%10 > lastDigit:
            isIncreasing = False
        if temp%10 == (temp//10)%10 and temp%10 == (temp//100)%10:
            digitToRemove = temp%10
            while digitToRemove == (temp//10)%10:
                temp = temp // 10
        lastDigit = temp%10
        temp = temp // 10
        if lastDigit == temp%10 and lastDigit != (temp//10)%10:
            isRepeating = True

    if isIncreasing and isRepeating:
        response += 1

pyperclip.copy(response)
#not working

#req = requests.Request('POST', "https://adventofcode.com/2018/day/1/answer")
#prepped = req.prepare()

#prepped.body = "level=1&answer="+response

#resp = s.send(prepped)

#print(resp.text)

print(response)
from copy import *

import pexpect
import time

child = pexpect.spawn('python day15_intcode.py')
child.delaybeforesend = None
child.readline()
child.readline()
commands = []
actualPosition = (0, 0)

def expected_position(number, actual_position):
    if number == 1:
        a = (actual_position[0], actual_position[1] - 1)
    if number == 2:
        a = (actual_position[0], actual_position[1] + 1)
    if number == 3:
        a = (actual_position[0] - 1, actual_position[1])
    if number == 4:
        a = (actual_position[0] + 1, actual_position[1])
    return a


def move(number, actual_position):
    global child
    child.sendline(str(number))
    child.readline()
    response_ = child.readline()
    response_ = int(response_)
    if response_ >= 1:
        next_position = expected_position(number, actual_position)
    else:
        next_position = actual_position
    return response_, next_position


def reverse(number, actual_position):
    if number == 1:
        return move(2, actual_position)
    if number == 2:
        return move(1, actual_position)
    if number == 3:
        return move(4, actual_position)
    if number == 4:
        return move(3, actual_position)


allPossibleCells = {}
oxygenMinutes = {}

def recursive_backtracking(number, actual_position):
    global oxygenPosition
    global allPossibleCells
    if actual_position not in allPossibleCells or allPossibleCells[actual_position] > number:
        allPossibleCells[actual_position] = number
        for i in range(1, 5):
            response, next_position = move(i, actual_position)
            #to do: oxygen condition
            if response == 2:
                oxygenPosition = next_position
            if next_position != actual_position:
                recursive_backtracking(number+1, next_position)
                reverse(i, next_position)


recursive_backtracking(0, actualPosition)



#def recursiveAsign(coordinates)

for i in list(allPossibleCells.keys()):
    oxygenMinutes[i] = 999

oxygenMinutes[oxygenPosition] = 0

to_polish = True

while to_polish:
    to_polish = False
    for i in oxygenMinutes.keys():
        if (i[0] + 1, i[1]) in oxygenMinutes.keys():
            if oxygenMinutes[(i[0] + 1, i[1])] > oxygenMinutes[i]+1:
                oxygenMinutes[(i[0] + 1, i[1])] = oxygenMinutes[i]+1
                to_polish = True
        if (i[0] - 1, i[1]) in oxygenMinutes.keys():
            if oxygenMinutes[(i[0] - 1, i[1])] > oxygenMinutes[i]+1:
                oxygenMinutes[(i[0] - 1, i[1])] = oxygenMinutes[i]+1
                to_polish = True
        if (i[0], i[1] + 1) in oxygenMinutes.keys():
            if oxygenMinutes[(i[0], i[1] + 1)] > oxygenMinutes[i]+1:
                oxygenMinutes[(i[0], i[1] + 1)] = oxygenMinutes[i]+1
                to_polish = True
        if (i[0], i[1] - 1) in oxygenMinutes.keys():
            if oxygenMinutes[(i[0], i[1] - 1)] > oxygenMinutes[i]+1:
                oxygenMinutes[(i[0], i[1] - 1)] = oxygenMinutes[i]+1
                to_polish = True

response = max(list(oxygenMinutes.values()))

assert response < 388
print(response)

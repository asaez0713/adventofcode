import numpy as np

f = open('2.txt','r')

data = f.readlines()[:-1]
data = [string[:-1] for string in data]

pos = np.array([1,1])

def move(char):
    global pos
    if char == 'L' and pos[0] > 0:
        pos += np.array([-1,0])
    if char == 'R' and pos[0] < 2:
        pos += np.array([1,0])
    if char == 'U' and pos[1] < 2:
        pos += np.array([0,1])
    if char == 'D' and pos[1] > 0:
        pos += np.array([0,-1])

def get_digit(pos):
    if pos[0] == 0:
        if pos[1] == 0:
            return 7
        elif pos[1] == 1:
            return 4
        elif pos[1] == 2:
            return 1
    elif pos[0] == 1:
        if pos[1] == 0:
            return 8
        elif pos[1] == 1:
            return 5
        elif pos[1] == 2:
            return 2
    elif pos[0] == 2:
        if pos[1] == 0:
            return 9
        elif pos[1] == 1:
            return 6
        elif pos[1] == 2:
            return 3

for string in data:
    for char in string:
        move(char)
    print(get_digit(pos))

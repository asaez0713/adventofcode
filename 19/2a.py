import math
import numpy as np

f = open('2.in','r')
data = f.readlines()
data = data[0].strip().split(',')
data = [int(num) for num in data]

data[1] = 12
data[2] = 2
place = 0

opcode = data[place]
pos1 = data[place+1]
pos2 = data[place+2]
pos3 = data[place+3]

while opcode != 99:
    if opcode == 1:
        data[pos3] = data[pos1] + data[pos2]
    elif opcode == 2:
        data[pos3] = data[pos1] * data[pos2]
    elif opcode == 99:
        break
    
    place += 4
    opcode = data[place]
    pos1 = data[place+1]
    pos2 = data[place+2]
    pos3 = data[place+3]


print(data[0])

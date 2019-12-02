import math
import numpy as np

f = open('1.in','r')

data = f.readlines()
data = [int(string.strip()) for string in data]

tot_fuel = 0

for num in data:
    temp = int(num)
    while temp > 0:
        temp //= 3
        temp -= 2
        if temp > 0:
            tot_fuel += temp

print(tot_fuel)

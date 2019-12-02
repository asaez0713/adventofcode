import math
import numpy as np

f = open('1.in','r')

data = f.readlines()
data = [int(string.strip()) for string in data]

tot_fuel = 0

for num in data:
    tot_fuel += (num//3) - 2

print(tot_fuel)

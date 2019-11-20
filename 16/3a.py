import numpy as np
import re

f = open('3.txt','r')

data = f.readlines()[:-1]
data = [re.split(r'\s+', item[2:-2].strip()) for item in data]

data = [[int(x) for x in lst] for lst in data]

count = 0

for lst in data:
    lst.sort()
    if lst[0] + lst[1] > lst[2]:
        count += 1
    else:
        pass

print(count)

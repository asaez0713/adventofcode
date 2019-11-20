import re
import numpy as np

f = open('1.txt','r')

data = f.readline().split(', ')

right = re.compile(r'R(?P<right>\d+)')
left = re.compile(r'L(?P<left>\d+)')

face_dir = 0
pos = np.array([0.0,0.0])

def step(face,step_num,move_dir):
    global face_dir, pos
    move_vec = np.array([step_num*np.sign(move_dir),0.0])
    if face % 2 == 1:
        move_vec = move_vec[::-1]
    if face == 1 or face == 2:
        move_vec *= -1
    face_dir += move_dir
    face_dir %= 4
    pos += move_vec

for instruction in data:
    if right.search(instruction):
        move_dir = 1
    elif left.search(instruction):
        move_dir = -1
    step_num = float(instruction[1:])
    step(face_dir,step_num,move_dir)

print(sum(x for x in np.absolute(pos)))

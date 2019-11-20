import re
import numpy as np

f = open('1.txt','r')

data = f.readline().split(', ')

right = re.compile(r'R(?P<right>\d+)')
left = re.compile(r'L(?P<left>\d+)')

face_dir = 0
pos = np.array([0.0,0.0])
temp = np.array([0.0,0.0])
ew_moves = []
ns_moves = []

def check_cross(ew_move,ns_move):
    x0 = ew_move[0][0]
    x1 = ew_move[1][0]
    xcheck = ns_move[0][0]
    y0 = ns_move[0][1]
    y1 = ns_move[1][1]
    ycheck = ew_move[0][1]
    if x0 < xcheck < x1 or x1 < xcheck < x0:
        if y0 < ycheck < y1 or y1 < ycheck < y0:
            return True
    return False

def step(face,step_num,move_dir):
    global face_dir, temp, pos
    move_vec = np.array([step_num*np.sign(move_dir),0.0])
    if face % 2 == 1:
        move_vec = move_vec[::-1]
    if face == 1 or face == 2:
        move_vec *= -1
    face_dir += move_dir
    face_dir %= 4
    temp = list(pos)
    pos += move_vec

for instruction in data:
    if right.search(instruction):
        move_dir = 1
    elif left.search(instruction):
        move_dir = -1
    step_num = float(instruction[1:])
    step(face_dir,step_num,move_dir)
    if face_dir % 2 == 1:
        for move in ns_moves:
            if check_cross([temp,pos],move):
                cross = np.array([temp[0],move[0][1]])
                print(sum(x for x in np.absolute(cross)))
                exit(0)
        ew_moves.append([list(temp),list(pos)])
    elif face_dir % 2 == 0:
        for move in ew_moves:
            if check_cross(move,[temp,pos]):
                cross = np.array([temp[0],move[0][1]])
                print(sum(x for x in np.absolute(cross)))
                exit(0)
        ns_moves.append([list(temp),list(pos)])

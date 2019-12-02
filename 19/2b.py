f = open('2.in','r')
data = f.readlines()
data = data[0].strip().split(',')
data = [int(num) for num in data]

for noun in range(len(data)):
    for verb in range(len(data)):
        try_lst = list(data)
        try_lst[1] = noun
        try_lst[2] = verb
        place = 0

        opcode = try_lst[place]
        pos1 = try_lst[place+1]
        pos2 = try_lst[place+2]
        pos3 = try_lst[place+3]

        while opcode != 99:
            if opcode == 1:
                try_lst[pos3] = try_lst[pos1] + try_lst[pos2]
            elif opcode == 2:
                try_lst[pos3] = try_lst[pos1] * try_lst[pos2]
            elif opcode == 99:
                break
            
            place += 4
            opcode = try_lst[place]
            pos1 = try_lst[place+1]
            pos2 = try_lst[place+2]
            pos3 = try_lst[place+3]
        
        if try_lst[0] == 19690720:
            print(100*noun + verb)
            exit(0)

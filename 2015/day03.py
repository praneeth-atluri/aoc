with open('2015/day03.txt') as f:
    directions = f.read()

    # print(directions)

history = [(0,0)]

for i in range(len(directions)):
    last = history[-1]
    if directions[i]=='v':
        history.append((last[0],last[1]-1))
    elif directions[i]=='^':
        history.append((last[0],last[1]+1))
    elif directions[i]=='>':
        history.append((last[0]+1,last[1]))
    elif directions[i]=='<':
        history.append((last[0]-1,last[1]))



unique_locations = len(set(history))
print(unique_locations)




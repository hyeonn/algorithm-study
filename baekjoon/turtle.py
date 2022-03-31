dx = [0,-1,0,1]
dy = [1,0,-1,0]

n = int(input())

for i in range(n):
    x = 0
    y = 0
    direc = 0
    tc = input()
    trace = [(0, 0)]      # (x,y)
    for j in tc:
        if j == 'F':
            x = x + dx[direc]
            y = y + dy[direc]
        elif j == 'B':
            x = x - dx[direc]
            y = y - dy[direc]
        elif j == 'L':
            if direc == 3:
                direc = 0
            else:
                direc += 1
        elif j == 'R':
            if direc == 0:
                direc = 3
            else:
                direc -= 1
        trace.append((x, y))
    len_x = max(trace, key = lambda x:x[0])[0]  - min(trace, key = lambda x:x[0])[0]
    len_y = max(trace, key = lambda x:x[1])[1]  - min(trace, key = lambda x:x[1])[1]

    print(len_x*len_y)
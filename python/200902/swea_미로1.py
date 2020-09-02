def BFS(x,y):
    Q.append((x,y))
    V[x][y] = 1
    while Q:
        x, y = Q.pop(0)
        if arr[x][y] == '3': return 1
        for x1, y1 in drs:
            if arr[x+x1][y+y1] != '1' and not V[x+x1][y+y1]:
                Q.append((x+x1,y+y1))
                V[x+x1][y+y1] = 1
    return 0

for _ in range(10):
    t = int(input())
    arr = [input() for _ in range(16)]
    Q, V = [], [[0]*16 for _ in range(16)]
    drs, result = [(1,0),(-1,0),(0,1),(0,-1)], 0
    for i in range(1,15):
        for j in range(1,15):
            if arr[i][j] == '2':
                result = BFS(i,j)
                break
        if result: break
    print(f'#{t} {result}')
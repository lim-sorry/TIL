def BFS(x,y,c):
    Q.append((x,y))
    V[x][y] = c
    cnt = 1
    while Q:
        x,y = Q.pop(0)
        for x1,y1 in drs:
            if arr[x+x1][y+y1] == '1' and not V[x+x1][y+y1]:
                Q.append((x+x1,y+y1))
                V[x+x1][y+y1] = 1
                cnt += 1
    return cnt

N = int(input())
arr = ['0'*(N+2)]+['0'+input()+'0' for _ in range(N)]+['0'*(N+2)]
V = [[0]*(N+2) for _ in range(N+2)]
drs = [(1,0),(0,1),(-1,0),(0,-1)]
Q, c, result = [], 1, []
for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j] == '1' and not V[i][j]:
            result.append(BFS(i,j,c))
            c += 1
print(c-1)
for i in sorted(result): print(i)
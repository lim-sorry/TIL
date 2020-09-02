def BFS(x,y):
    Q.append((x,y))
    V[x][y] = 1
    while Q:
        x,y = Q.pop(0)
        if arr[x][y] == '3': return V[x][y]-2
        for x1,y1 in drs:
            if arr[x+x1][y+y1] != '1' and not V[x+x1][y+y1]:
                Q.append((x+x1,y+y1))
                V[x+x1][y+y1] = V[x][y] + 1
    return '0'

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = ['1'*(N+2)]+['1'+input()+'1' for _ in range(N)]+['1'*(N+2)]
    drs = [(-1,0),(0,1),(1,0),(0,-1)]
    Q, V, result = [], [[0]*(N+2) for _ in range(N+2)], 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if arr[i][j] == '2':
                result = BFS(i,j)
                break
        if result: break
    print(f'#{t} {result}')


"""
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000
"""
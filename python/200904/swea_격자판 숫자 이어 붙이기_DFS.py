def DFS(x,y,K=0,S=''):
    if K == 6:
        S += arr[x][y]
        if S not in result: result.append(S)
        return
    else:
        S += arr[x][y]
        for x1,y1 in [(1,0),(-1,0),(0,1),(0,-1)]:
            if 0 <= x+x1 <= 3 and 0 <= y+y1 <= 3:
                DFS(x+x1,y+y1,K+1,S)

T = int(input())
for t in range(1,T+1):
    arr = [input().replace(' ','') for _ in range(4)]
    stack, result = [], []
    for i in range(4):
        for j in range(4):
            DFS(i,j)
    print(f'#{t} {len(result)}')
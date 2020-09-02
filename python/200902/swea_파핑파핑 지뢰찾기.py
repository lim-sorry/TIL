def Mine(i,j):
    global result
    cnt = 0
    for x, y in drs:
        if arr[i+x][j+y] == '.': cnt += 1
    if cnt == 9:
        Q.append((i,j))
        V[i][j] = 1
        while Q:
            cnt = 0
            i, j = Q.pop(0)
            for x, y in drs:
                if arr[i+x][j+y] == '.': cnt += 1
            if cnt == 9:
                for x, y in drs:
                    if not V[i+x][j+y] and 1<=i+x<=N and 1<=j+y<=N:
                        Q.append((i+x,j+y))
                        V[i+x][j+y] = 1
        result += 1


T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = ['.'*(N+2)] + ['.'+input()+'.' for _ in range(N)] + ['.'*(N+2)]
    drs = [(1,1),(1,0),(1,-1),(0,1),(0,0),(0,-1),(-1,1),(-1,0),(-1,-1)]
    Q, V = [], [[0]*(N+2) for _ in range(N+2)]
    result = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if not V[i][j]:
                Mine(i,j)
    for i in range(1,N+1):
        for j in range(1,N+1):
            if not V[i][j] and arr[i][j] == '.':
                result += 1
    print(f'#{t} {result}')
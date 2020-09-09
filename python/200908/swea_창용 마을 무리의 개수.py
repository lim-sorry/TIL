def BFS(i,cnt):
    Q = [-1]*(N+1)
    F = R = 0
    Q[R], R = i, R+1
    V[i] = cnt
    while F != R:
        i, F = Q[F], F+1
        for j in range(N):
            if arr[i][j] and not V[j]:
                Q[R], R = j, R+1
                V[j] = cnt

T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    arr = [[0]*N for _ in range(N)]
    V = [0]*N
    for _ in range(M):
        x, y = map(lambda x:int(x)-1,input().split())
        arr[x][y] = 1
        arr[y][x] = 1
    cnt = 1
    for i in range(N):
        if not V[i]:
            BFS(i, cnt)
            cnt += 1
    print(f'#{t} {cnt-1}')
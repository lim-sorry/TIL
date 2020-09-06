def Count():
    for i in range(N):
        for j in range(M):
            if not arr[i][j]: return True

M, N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
Q, cnt, = [None]*(N*M) , 1
F, R = 0, 0
if Count():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                Q[R] = (i,j)
                R += 1
    while F != R:
        i, j = Q[F]
        F += 1
        for k, l in [(1,0),(-1,0),(0,1),(0,-1)]:
            if 0 <= i+k < N and 0 <= j+l < M and arr[i+k][j+l] == 0:
                Q[R] = (i+k,j+l)
                R += 1
                arr[i+k][j+l] = arr[i][j]+1
                cnt = arr[i][j] + 1
    if Count(): cnt = 0
print(cnt-1)
import sys

def Count():
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if arr[h][n][m] == 0: return True

M, N, H = map(int,sys.stdin.readline().split())
arr = [[list(map(int,sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
if Count():
    Q = [0]*(M*N*H)
    F = R = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if arr[h][n][m] == 1:
                    Q[R] = (h,n,m)
                    R += 1
    while F != R:
        h, n, m = Q[F]
        F += 1
        for dr in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
            if 0 <= h+dr[0] < H and 0 <= n+dr[1] < N and 0 <= m+dr[2] < M:
                if arr[h+dr[0]][n+dr[1]][m+dr[2]] == 0:
                    Q[R] = (h+dr[0],n+dr[1],m+dr[2])
                    arr[h+dr[0]][n+dr[1]][m+dr[2]] = arr[h][n][m]+1
                    result = arr[h+dr[0]][n+dr[1]][m+dr[2]]-1
                    R += 1
    if Count(): result = -1
else: result = 0
print(result)
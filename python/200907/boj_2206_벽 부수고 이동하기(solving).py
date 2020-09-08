import sys

def BFS():
    Q = [0]*(N*M*2)
    F = R = 0
    Q1 = [0]*(N*M)
    F1 = R1 = 0
    if arr[0][0] == '0':
        Q[R] = (0,0)
        arr[0][0] = 1
        R += 1
    else:
        Q1[R1] = (0,0)
        arr[0][0] = 1
        R1 += 1
    while F != R:
        n, m = Q[F]
        F += 1
        for dr in ((1,0),(-1,0),(0,1),(0,-1)):
            if 0 <= n+dr[0] < N and 0 <= m+dr[1] < M:
                if arr[n+dr[0]][m+dr[1]] == '0':
                    Q[R] = (n+dr[0],m+dr[1])
                    arr[n+dr[0]][m+dr[1]] = arr[n][m]+1
                    R += 1
                elif arr[n+dr[0]][m+dr[1]] == '1':
                    Q1[R1] = (n+dr[0],m+dr[1])
                    arr[n+dr[0]][m+dr[1]] = arr[n][m]+1
                    R1 += 1
    while F1 != R1:
        n, m = Q1[F1]
        F1 += 1
        for dr in ((1,0),(-1,0),(0,1),(0,-1)):
            if 0 <= n+dr[0] < N and 0 <= m+dr[1] < M:
                if arr[n+dr[0]][m+dr[1]] == '0' or int(arr[n+dr[0]][m+dr[1]]) > arr[n][m]+1:
                    Q[R] = (n+dr[0],m+dr[1])
                    arr[n+dr[0]][m+dr[1]] = arr[n][m]+1
                    R += 1
    while F != R:
        n, m = Q[F]
        F += 1
        for dr in ((1,0),(-1,0),(0,1),(0,-1)):
            if 0 <= n+dr[0] < N and 0 <= m+dr[1] < M:
                if arr[n+dr[0]][m+dr[1]] == '0' or int(arr[n+dr[0]][m+dr[1]]) > arr[n][m]+1:
                    Q[R] = (n+dr[0],m+dr[1])
                    arr[n+dr[0]][m+dr[1]] = arr[n][m]+1
                    R += 1
    return arr[N-1][M-1]

N, M = map(int,sys.stdin.readline().split())
arr = [list(sys.stdin.readline())[:-1] for _ in range(N)]
print(BFS())
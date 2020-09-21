import sys

N, M = map(int,sys.stdin.readline().split())
arr = [list(sys.stdin.readline())[:-1] for _ in range(N)]
V = [[0]*M for _ in range(N)]
Q, F, R = [0]*(N*M+1), 0, 0
Q2, F2, R2 = [0]*(2*N*M+2), 0, 0
Q[R], R = (0,0), R+1
V[0][0] = 1
result = []
while F != R:
    (i,j), F = Q[F], F+1
    if (i,j) == (N-1,M-1):
        result.append(V[i][j])
        break
    for dr in [(1,0),(-1,0),(0,1),(0,-1)]:
        if 0 <= i+dr[0] < N and 0 <= j+dr[1] < M:
            if not V[i+dr[0]][j+dr[1]]:
                if arr[i+dr[0]][j+dr[1]] == '1': Q2[R2], R2 = (i+dr[0],j+dr[1]), R2+1
                else: Q[R], R = (i+dr[0],j+dr[1]), R+1
                V[i+dr[0]][j+dr[1]] = V[i][j]+1
while F2 != R2:
    (i,j), F2 = Q2[F2], F2+1
    if (i,j) == (N-1,M-1):
        result.append(V[i][j])
    for dr in [(1,0),(-1,0),(0,1),(0,-1)]:
        if 0 <= i+dr[0] < N and 0 <= j+dr[1] < M:
            if arr[i+dr[0]][j+dr[1]] == '0':
                if not V[i+dr[0]][j+dr[1]] or V[i+dr[0]][j+dr[1]] > V[i][j]+1:
                    Q2[R2], R2 = (i+dr[0],j+dr[1]), R2+1
                    V[i+dr[0]][j+dr[1]] = V[i][j]+1
if result: print(min(result))
else: print(-1)
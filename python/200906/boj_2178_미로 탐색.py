def BFS():
    Q = [(0,0)]
    visit[0][0] = 1
    while Q:
        i, j = Q.pop(0)
        if (i,j) == (N-1,M-1):
            return visit[i][j]
        for k, l in [(1,0),(0,1),(-1,0),(0,-1)]:
            if 0 <= i+k < N and 0 <= j+l < M:
                if arr[i+k][j+l] == '1' and not visit[i+k][j+l]:
                    Q.append((i+k,j+l))
                    visit[i+k][j+l] = visit[i][j] + 1

N, M = map(int,input().split())
arr = [input() for _ in range(N)]
visit = [[0]*M for _ in range(N)]
print(BFS())
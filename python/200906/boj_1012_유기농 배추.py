def BFS(i,j):
    Q.append((i,j))
    visit[i][j] = cnt
    while Q:
        i, j = Q.pop(0)
        for k, l in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0 <= i+k < N and 0 <= j+l < M:
                if arr[i+k][j+l] and not visit[i+k][j+l]:
                    Q.append((i+k,j+l))
                    visit[i+k][j+l] = cnt

T = int(input())
for t in range(1,T+1):
    M, N, K = map(int,input().split())
    arr = [[0]*M for _ in range(N)]
    Q, visit, cnt = [], [[0]*M for _ in range(N)], 0
    for _ in range(K):
        x, y = map(int,input().split())
        arr[y][x] = 1
    for i in range(N):
        for j in range(M):
            if arr[i][j] and not visit[i][j]:
                cnt += 1
                BFS(i,j)
    print(cnt)
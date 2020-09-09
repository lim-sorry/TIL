def Count(i,j):
    Q = [-1]*(N**2+1)
    F = R = 0
    Q[R] = (i,j)
    R += 1
    cnt, min_num = 0, arr[i][j]
    while F != R:
        i, j = Q[F]
        F += 1
        for dr in [(1,0),(-1,0),(0,1),(0,-1)]:
            if 0 <= i+dr[0] < N and 0 <= j+dr[1] < N and not V[i+dr[0]][j+dr[1]]:
                if abs(arr[i+dr[0]][j+dr[1]]-arr[i][j]) == 1:
                    Q[R] = (i+dr[0],j+dr[1])
                    R += 1
                    V[i+dr[0]][j+dr[1]] = 1
                    cnt += 1
                    min_num = min(arr[i+dr[0]][j+dr[1]],min_num)
    if cnt > result[1]: return [min_num,cnt]
    elif cnt == result[1]: return [min(min_num,result[0]),cnt]
    return result

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    V = [[0]*N for _ in range(N)]
    result = [0, 0]
    for i in range(N):
        for j in range(N):
            if not V[i][j]: result = Count(i,j)
    print(f'#{t} {result[0]} {result[1]}')

"""
2
2
1 2
3 4
3
9 3 4
6 1 5
7 8 2
"""

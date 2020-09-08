def DFS(n=0,k=0,t=0):
    if k == N//2:
        result.append(abs(T-t))
        return
    if n == N: return
    V[n] = 0
    DFS(n+1,k,t)
    V[n] = 1
    t += sum(arr[n][i] + arr[i][n] for i in range(N))
    DFS(n+1,k+1,t)

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    V = [0]*N
    result = []
    T = sum(sum(row) for row in arr)
    DFS()
    print(f'#{t} {min(result)}')

"""
3
4
0 5 3 8
4 0 4 1
2 5 0 3
7 2 3 0
4
0 7 1 1
7 0 6 2
1 1 0 2
10 1 9 0
6
0 37 26 52 77 20
32 0 15 26 75 16
54 33 0 79 37 90
92 10 66 0 92 3
64 7 89 89 0 21
80 49 94 68 5 0
"""
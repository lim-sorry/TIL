def DFS(n=0,s=0):
    if n == N:
        if s >= B and result[0] > s: result[0] = s
        return
    if s > result[0]: return
    DFS(n+1,s)
    DFS(n+1,s+arr[n])

T = int(input())
for t in range(1,T+1):
    N, B = map(int,input().split())
    arr = list(map(int,input().split()))
    result = [sum(arr)]
    DFS()
    print(f'#{t} {result[0]-B}')
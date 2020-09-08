def DFS(n=0,p=1):
    global result
    if n == N:
        result = p if result < p else result
        return
    if p <= result: return
    for i in range(N):
        if assign[i] == 0:
            assign[i] = 1
            DFS(n+1,p*arr[n][i])
            assign[i] = 0

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(lambda x: int(x)/100,input().split())) for _ in range(N)]
    result = 0
    assign = [0]*N
    DFS()
    print("#%d %.6f" % (t, result*100))
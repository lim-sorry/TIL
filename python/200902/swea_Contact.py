def Contact(S):
    Q.append(S)
    V[S] = 1
    while Q:
        S = Q.pop(0)
        for i in range(100):
            if arr[S][i] and not V[i]:
                Q.append(i)
                V[i] = V[S]+1

for t in range(1,11):
    N, S = map(int,input().split())
    D = list(map(lambda x:int(x)-1,input().split()))
    arr = [[0]*100 for _ in range(100)]
    Q, V, maxV = [], [0]*100, 0
    for i in range(0,N,2):
        arr[D[i]][D[i+1]] = 1
    Contact(S-1)
    for i in range(100):
        if V[maxV] <= V[i]: maxV = i
    print(f'#{t} {maxV+1}')
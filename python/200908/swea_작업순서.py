for t in range(1,11):
    V, E = map(int,input().split())
    route = list(map(int,input().split()))
    arr = [[0]*(V+1) for _ in range(V+1)]
    for i in range(0,2*E,2):
        arr[route[i]][route[i+1]] = 1
        arr[route[i+1]][route[i]] = -1
    Q = [-1]*(V+1)
    F = R = 0
    for i in range(V,0,-1):
        if -1 not in arr[i]:
            Q[R], R = str(i), R+1
    while Q[V-1] == -1:
        i, F = int(Q[F]), F+1
        for j in range(V,0,-1):
            arr[j][i] = 0
            if (arr[i][j] == 1) and (-1 not in arr[j]):
                Q[R], R = str(j), R+1
    print(f'#{t} {" ".join(Q[:-1])}')
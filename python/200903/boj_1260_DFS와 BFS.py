def DFS(S):
    stack.append(S)
    visit[S] = 1
    for E in range(1,N+1):
        if arr[S][E] and not visit[E]:
            DFS(E)
    if S == V: return stack

def BFS(S):
    Q.append(S)
    F, R = 0, 1
    visit[S] = 1
    while F != R:
        S = Q[F]
        F += 1
        for E in range(1,N+1):
            if arr[S][E] and not visit[E]:
                Q.append(E)
                R += 1
                visit[E] = 1
    return Q

N, M, V = map(int,input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    X, Y = map(int,input().split())
    arr[X][Y] = 1
    arr[Y][X] = 1
stack, visit = [], [0 for _ in range(N+1)]
print(' '.join(map(str,DFS(V))))
Q, visit = [], [0 for _ in range(N+1)]
print(' '.join(map(str,BFS(V))))
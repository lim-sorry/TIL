def BFS():
    Q = [0]*100001
    V = [0]*100001
    F, R = 0, 1
    Q[F] = N
    V[N] = 1
    while F != R:
        n = Q[F]
        F += 1
        if n == K: return V[n]-1
        for i in (n-1,n+1,n*2):
            if 0 <= i <= 100000 and not V[i]:
                Q[R] = i
                V[i] = V[n] + 1
                R += 1

N, K = map(int,input().split())
print(BFS())
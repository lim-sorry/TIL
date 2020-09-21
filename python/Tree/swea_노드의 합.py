def f(n):
    if n*2 <= N: arr[n] += f(n*2)
    if n*2+1 <= N: arr[n] += f(n*2+1)
    return arr[n]

T = int(input())
for t in range(1,T+1):
    N, M, L = map(int,input().split())
    arr = [0]*(N+1)
    for _ in range(M):
        n, m = map(int,input().split())
        arr[n] = m
    print(f'#{t} {f(L)}')
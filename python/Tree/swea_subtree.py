def f(n):
    result.append(n)
    for i in arr[n]: f(i)
 
T = int(input())
for t in range(1,T+1):
    N, S = map(int,input().split())
    edges = list(map(int,input().split()))
    arr, result = [[] for _ in range(N+2)], []
    for i in range(N):
        arr[edges[2*i]].append(edges[2*i+1])
    f(S)
    print(f'#{t} {len(result)}')
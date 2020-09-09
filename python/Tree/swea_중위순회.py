def f(n):
    if arr[n][0]: f(arr[n][0])
    result.append(arr[n][1])
    if arr[n][2]: f(arr[n][2])

for t in range(1,11):
    N = int(input())
    arr = [None for _ in range(N+1)]
    for _ in range(N):
        n,c,l,r = list(input().split()+[0,0])[:4]
        arr[int(n)] = [int(l),c,int(r)]
    result = []
    f(1)
    print(f'#{t} {"".join(result)}')
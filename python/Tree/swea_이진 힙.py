def heap(n):
    if n == 1: return
    if arr[n//2] > arr[n]:
        arr[n//2], arr[n] = arr[n], arr[n//2]
        heap(n//2)

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [0]+list(map(int,input().split()))
    for i in range(2,N+1): heap(i)
    result = 0
    while N > 0:
        N //= 2
        result += arr[N]
    print(f'#{t} {result}')
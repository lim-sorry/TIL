def f(n):
    global cnt
    if n > N: return
    f(n*2)
    arr[n] = cnt
    cnt += 1
    f(n*2+1)

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [0]*(N+1)
    cnt = 1
    f(1)
    print(f'#{t} {arr[1]} {arr[N//2]}')
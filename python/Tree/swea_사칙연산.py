def f(n):
    if arr[n][1].isnumeric(): return int(arr[n][1])
    a = f(int(arr[n][2]))
    b = f(int(arr[n][3]))
    if arr[n][1] == '+': return a + b
    elif arr[n][1] == '-': return a - b
    elif arr[n][1] == '*': return a * b
    else: return a // b

for t in range(1,11):
    N = int(input())
    arr = [None]+[input().split() for _ in range(N)]
    print(f'#{t} {f(1)}')
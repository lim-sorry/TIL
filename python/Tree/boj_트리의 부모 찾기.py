import sys
sys.setrecursionlimit(10 ** 9)

def f(n):
    V[n] = 1
    for i in arr[n]:
        if V[i]: result[n] = str(i)
        else: f(i)

N = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    n1, n2 = map(int,input().split())
    arr[n1] += [n2]
    arr[n2] += [n1]
V = [0]*(N+1)
result = [0]*(N+1)
f(1)
print('\n'.join(result[2:]))
import sys

def f(n,s=0):
    visit[n] = 1
    if s and len(arr[n]) == 2:
        result.append(s)
        return
    for i in range(0,len(arr[n]),2):
        if not visit[arr[n][i]]:
            f(arr[n][i],s+arr[n][i+1])
            visit[arr[n][i]] = 0
    visit[n] = 0

V = int(sys.stdin.readline())
arr = [[] for _ in range(V+1)]
visit = [0]*(V+1)
for _ in range(V):
    nlist = list(map(int,sys.stdin.readline().split()))
    for i in range(1,len(nlist)-1,2):
        arr[nlist[0]] += [nlist[i],nlist[i+1]]
result = []
for i in range(1,V+1): f(i,0)
print(max(result))
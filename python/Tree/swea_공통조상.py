from collections import deque
 
def f(n):
    result.append(n)
    for i in tree[n]: f(i)
 
for tc in range(int(input())):
    V, E, T1, T2 = map(int,input().split())
    tree, parent = [[] for _ in range(V+1)], [0]*(V+1)
    nlist = deque(map(int,input().split()))
    while nlist:
        p, c = nlist.popleft(), nlist.popleft()
        tree[p].append(c)
        parent[c] = p
    parents = []
    while parent[T1]:
        parents.append(parent[T1])
        T1 = parent[T1]
    while parent[T2] not in parents:
        T2 = parent[T2]
    result = []
    f(parent[T2])
    print(f'#{tc+1} {parent[T2]} {len(result)}')
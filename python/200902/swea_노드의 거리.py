def BFS(S,G):
    Q.append(S)
    Visit[S] = 1
    while Q:
        n = Q.pop(0)
        if n == G: return Visit[n]-1
        for i in range(V):
            if arr[n][i] and not Visit[i]:
                Q.append(i)
                Visit[i] = Visit[n] + 1
    return 0

T = int(input())
for t in range(1,T+1):
    V, E = map(int,input().split())
    arr = [[0]*V for _ in range(V)]
    for _ in range(E):
        n1, n2 = map(lambda x:int(x)-1,input().split())
        arr[n1][n2] = 1
        arr[n2][n1] = 1
    S, G = map(lambda x:int(x)-1,input().split())
    Q, Visit = [], [0]*V
    print(f'#{t} {BFS(S,G)}')


"""
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
1 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9
"""
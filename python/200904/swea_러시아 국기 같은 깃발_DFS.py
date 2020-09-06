def DFS(K=0,T=0):
    if T > result[-1]: return
    elif K == N:
        if stack[-1] == 'R': result.append(T)
        return
    elif K == 0:
        stack.append('W')
        DFS(K+1,T+M-arr[K].count('W'))
        stack.pop()
        return result[-1]
    else:
        avail = 'WB' if stack[-1] == 'W' else 'BR' if stack[-1] == 'B' else 'R'
        for C in avail:
            stack.append(C)
            DFS(K+1,T+M-arr[K].count(C))
            stack.pop()

T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    arr = [input() for _ in range(N)]
    stack, result = [], [N*M]
    print(f'#{t} {DFS()}')
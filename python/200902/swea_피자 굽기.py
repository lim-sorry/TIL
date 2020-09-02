def Pizza():
    cnt = N
    while len(Q) > 1:
        s = Q.pop(0)
        C[s] = C[s]//2
        if C[s]: Q.append(s)
        elif cnt < M:
            Q.append(cnt)
            cnt += 1
    return Q.pop(0)

T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    C = list(map(int,input().split()))
    Q = list(range(N))
    print(f'#{t} {Pizza()+1}')


"""
3
3 5
7 2 6 5 3
5 10
5 9 3 9 9 2 5 8 7 1
5 10
20 4 5 7 3 15 2 1 2 2
"""
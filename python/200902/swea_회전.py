T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    Q = list(map(int,input().split()))
    for _ in range(M): Q.append(Q.pop(0))
    print(f'#{t} {Q[0]}')

"""
3
3 10
5527 731 31274
5 12
18140 14618 18641 22536 23097
10 23
17236 31594 29094 2412 4316 5044 28515 24737 11578 7907
"""
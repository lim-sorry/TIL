# 18258 큐 2

import sys

N = int(input())
Q, F, R = [0]*2000000, 0, 0
for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        Q[R] = order[1]
        R += 1
    elif order[0] == 'pop':
        if F != R:
            print(Q[F])
            F += 1
        else: print(-1)
    elif order[0] == 'size':
        print(R-F)
    elif order[0] == 'empty':
        print(1) if F == R else print(0)
    elif order[0] == 'front':
        print(Q[F]) if F != R else print(-1)
    else:
        print(Q[R-1]) if F != R else print(-1)
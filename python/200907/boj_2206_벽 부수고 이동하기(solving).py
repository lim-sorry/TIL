import sys

N, M = map(int,sys.stdin.readline().split())
arr = [list(sys.stdin.readline())[:-1] for _ in range(N)]
print(BFS())
N = int(input())
Q = []
for i, n in enumerate(list(map(int,input().split()))):
    Q.insert(len(Q)-n,str(i+1))
print(' '.join(Q))
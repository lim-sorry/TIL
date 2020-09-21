N = int(input())
arr = [[0]*100 for _ in range(100)]
cnt = 0
for _ in range(N):
    X, Y = map(int,input().split())
    for i in range(X,X+10):
        for j in range(Y,Y+10):
            if not arr[i][j]:
                arr[i][j] = 1
                cnt += 1
print(cnt)
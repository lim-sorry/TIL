def Bingo(i,j):
    cnt = 0
    arr[i][j] = 0
    if not sum(arr[i]):
        cnt += 1
    if not sum([arr[k][j] for k in range(5)]):
        cnt += 1
    if i == j and not sum([arr[k][k] for k in range(5)]):
        cnt += 1
    if i == 4-j and not sum([arr[k][4-k] for k in range(5)]):
        cnt += 1
    return cnt

arr = [list(map(int,input().split())) for _ in range(5)]
nlist = []
for _ in range(5):
    nlist.extend(list(map(int,input().split())))
total = 0
for idx, n in enumerate(nlist):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == n:
                total += Bingo(i,j)
    if total >= 3:
        print(idx+1)
        break

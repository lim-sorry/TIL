N = int(input())
arr = list(map(int,input().split()))
cnt, temp, max_cnt = 0, 0, 0
for i in range(1,N):
    if arr[i-1] <= arr[i]:
        cnt += 1
    else:
        if cnt > max_cnt:
            max_cnt = cnt
        cnt = 1
if cnt > max_cnt:
    max_cnt = cnt
print(max_cnt)
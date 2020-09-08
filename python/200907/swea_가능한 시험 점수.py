T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    score = [1]+[0]*9999
    max_num = 0
    for i in arr:
        Q = []
        for j in range(max_num+1):
            if score[j]:
                Q.append(i+j)
        max_num += i
        for q in Q:
            score[q] = 1
    print(f'#{t} {score[:max_num+1].count(1)}')
T = int(input())
for t in range(1,T+1):
    N, M, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ds = [(0,1),(1,0),(0,-1),(-1,0)]
    result = []
    # 사각형의 왼쪽 위 인덱스 i, j
    for i in range(0,N-K+1):
        for j in range(0,M-K+1):
            total = 0
            # 우, 하, 좌, 상 방향으로 K-1번씩 이동하며 총 4*(K-1)개의 숫자를 더한다.
            for d in ds:
                for _ in range(K-1):
                    i, j = i+d[0], j+d[1]
                    total += arr[i][j]
            # 합산 결과를 result에 넣는다.
            result.append(total)
    # result 리스트에서 최댓값과 최솟값의 차를 출력한다.
    print(f'#{t} {max(result)-min(result)}')
    
"""
3
3 3 3
1 2 3
4 5 6
7 8 9
4 4 3
2 3 4 3
5 6 7 8
9 7 9 7
1 2 4 5
6 5 4
11 75 97 9 36
14 33 72 12 57
44 77 38 98 67
38 30 69 16 48
45 29 35 64 56
23 75 48 87 45
"""
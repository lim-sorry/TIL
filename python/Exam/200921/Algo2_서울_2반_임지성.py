def Boom(i,j):
    print(i,j)
    # i, j 위치의 폭탄 카운트
    cnt = 1
    # 폭발 범위를 저장하고 arr에서 폭탄을 제거한다.
    rng, arr[i][j] = arr[i][j], 0
    # 동서남북으로 각각 폭발 범위만큼 폭탄을 확인한다.
    for d in [(-1,0),(0,1),(1,0),(0,-1)]:
        for k in range(1,rng+1):
            # arr의 범위를 벗어나지 않으면서 폭탄이 있다면 Boom 함수 실행한다.
            if 0 <= i+k*d[0] < N and 0 <= j+k*d[1] < N and arr[i+k*d[0]][j+k*d[1]]:
                # 함수의 결과값을 카운트에 더해나간다.
                cnt += Boom(i+k*d[0],j+k*d[1])
    # 카운트를 리턴한다. 최종적으로는 모든 카운트를 더한 값이 리턴된다.
    return cnt
T = int(input())
for t in range(1,T+1):
    N = int(input())
    R, C = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{t} {Boom(R,C)}')

"""
3
4
3 3
0 0 1 0
0 2 0 1
0 0 0 0
1 1 0 2
6
3 2
0 0 0 0 0 0
0 0 3 0 1 1
1 0 0 0 0 0
0 0 3 0 0 2
2 0 0 0 0 0
0 1 0 2 0 2
10
8 7
0 3 0 0 3 0 0 0 0 0
0 3 0 0 0 0 0 1 0 3
0 0 5 0 0 0 0 0 3 0
0 0 0 0 0 0 0 0 0 0
0 5 0 0 0 2 0 5 0 0
0 0 0 0 0 3 0 2 0 4
4 0 2 0 0 2 1 4 0 0
0 0 0 0 0 5 0 0 0 0
0 0 0 0 0 0 4 5 5 1
3 0 3 0 2 4 0 0 0 1
"""
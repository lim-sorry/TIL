def district(i, j):
    # 체크한 장소인지 검사
    if not chk[i][j]:
        # 체크하지 않았다면 체크
        chk[i][j] = 1
        # 연못이라면 인접한 연못에 district 함수를 실행
        if arr[i][j]:
            for dr in drs:
                # 인접한 연못이면서 체크되지 않은 곳을 체크
                if arr[i+dr[0]][j+dr[1]] and not chk[i+dr[0]][j+dr[1]]:
                    district(i+dr[0], j+dr[1])
            # 최종적으로 새롭게 발견된 연못이기 때문에 True를 반환
            return True
        # 연못이 아니라면 False 반환
        else: return False
    # 이미 체크한 장소라면 False를 반환
    return False

T = int(input())
for t in range(1, T+1):
    M, N, K = map(int, input().split())
    # 더미 행렬을 상하좌우에 붙여서 index 오류를 방지한다.
    arr = [[0]*(M+2) for _ in range(N+2)]
    chk = [[0]*(M+2) for _ in range(N+2)]
    # 인접여부를 검사할 상하좌우에 해당하는 리스트 drs를 생성
    drs = [(-1,0), (0,-1), (0,1), (1,0)]
    # 연못의 초기 갯수 0
    cnt = 0
    # 연못 좌표는 더미를 붙였기 때문에 index에 1을 더한다.
    for _ in range(K):
        X, Y = map(int, input().split())
        arr[Y+1][X+1] = 1
    # 1~N 행에 대해서 1~M 열에 대해서 district 함수를 실행
    for i in range(1, N+1):
        for j in range(1, M+1):
            # 만약 새롭게 발견한 연못이라면 True를 반환하여 cnt에 1을 더한다.
            cnt += 1 if district(i, j) else 0
    # cnt를 최종적으로 출력
    print(f'#{t} {cnt}')


"""
3
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 3
5 5
4 4
6 6
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0
"""
T = int(input())
for t in range(1, T+1):
    # input을 불러온다
    N, M, D = map(int, input().split())
    # None으로 채워진 N*N 행렬을 생성한다
    arr = [[0]*N for _ in range(N)]
    # N//2+1개의 동심사각형을 대상으로 안쪽부터 초기값 M부터 D씩 증가한 값을 넣는다
    # 이때 동심사각형의 번호인 i를 활용해서 사각형의 둘레만 따라서 값을 대입한다
    for i in range(N//2+1):                     
        for j in range(N//2-i,N//2+i+1):
            arr[j][N//2-i] = M + D*i
            arr[N//2-i][j] = M + D*i
            arr[j][N//2+i] = M + D*i
            arr[N//2+i][j] = M + D*i
    # string에 결과를 담아 출력한다.
    result = ''
    for i in range(N):
        result += f'{sum(arr[i])} '
    print(f'#{t} {result}')

"""
3
7 5 2
9 10 -3
9 100 100
"""
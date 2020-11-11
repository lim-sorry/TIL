def search():
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1': return arr[i][j-55:j+1]

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    code = search()
    valid = ['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
    result, valify = 0, 0
    for i in range(8):
        for idx, v in enumerate(valid):
            if not int(code[7*i:7*i+7], 2) ^ int(v, 2):
                result += idx
                valify += 3 * idx if i % 2 else idx
    if valify % 10: result = 0
    print(f'#{t} {result}')

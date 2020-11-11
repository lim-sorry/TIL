def Bin(S):
    if len(S) == 1: return int(S)
    if S[-1] == '1': return 2 * Bin(S[:-1]) + 1
    return 2 * Bin(S[:-1])

T = int(input())
for t in range(1, T+1):
    string = input()
    result = []
    for i in range(10):
        result.append(str(Bin(string[7*i:7*(i+1)])))
    print(f'#{t} {" ".join(result)}')
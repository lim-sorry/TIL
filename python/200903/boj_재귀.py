# 10872 팩토리얼

def Factorial(N):
    return 1 if N < 1 else N * Factorial(N-1)

print(Factorial(int(input())))


# 10870 피보나치 수 5

def Fibo(N):
    if len(memo) > N: return memo[N] 
    memo.append(Fibo(N-1) + Fibo(N-2))
    return memo[N]

memo = [0, 1]
print(Fibo(int(input())))


# 2447 별찍기-10

def Star(x,y,N):
    if N == 1:
        arr[x][y] = '*'
    else:
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    Star(x+i*N//3,y+j*N//3,N//3)

N = int(input())
arr = [[' ']*N for _ in range(N)]
Star(0,0,N)
for i in range(N): print(''.join(arr[i]))


# 11729 하노이 탑 이동 순서

def Hanoi(S,T,G,N):
    if N == 1:
        result.append(f'{S} {G}')
        return 1
    cnt = Hanoi(S,G,T,N-1) + 1
    result.append(f'{S} {G}')
    cnt += Hanoi(T,S,G,N-1)
    return cnt

N = int(input())
result = []
print(Hanoi(1,2,3,N))
print('\n'.join(result))
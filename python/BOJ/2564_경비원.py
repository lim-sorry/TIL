def Dist(i):
    if abs(arr[i][0]-arr[-1][0]) == X:
        return X+min(arr[i][1]+arr[-1][1],2*Y-arr[i][1]-arr[-1][1])
    elif abs(arr[i][1]-arr[-1][1]) == Y:
        return Y+min(arr[i][0]+arr[-1][0],2*X-arr[i][0]-arr[-1][0])
    else:
        return abs(arr[i][0]-arr[-1][0])+abs(arr[i][1]-arr[-1][1])

X,Y = map(int,input().split())
N = int(input())
arr = []
for _ in range(N+1):
    n,m = map(int,input().split())
    if n == 1:
        arr.append((m,0))
    elif n == 2:
        arr.append((m,Y))
    elif n == 3:
        arr.append((0,m))
    else:
        arr.append((X,m))
T = 0
for i in range(N):
    T += Dist(i)
print(T)
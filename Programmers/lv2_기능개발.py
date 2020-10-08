# 14.32
def solution(progresses, speeds):
    P, S = progresses, speeds
    answer = []
    while P:
        for i in range(len(P)):
            if P[i] < 100:
                P[i] += S[i]
        if P[0] >= 100:
            cnt = 0
            while P and P[0] >= 100:
                cnt += 1
                P.pop(0)
                S.pop(0)
            answer.append(cnt)
    return answer
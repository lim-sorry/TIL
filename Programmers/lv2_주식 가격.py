# 27:56
def solution(prices):
    Q = []
    answer = list(range(len(prices)))
    for i, p in enumerate(prices):
        for q in Q[::-1]:
            q[2] += 1
            if p < q[1]:
                answer[q[0]] = q[2]
                Q.remove(q)        
        Q.append([i,p,0])
    for q in Q:
        answer[q[0]] = q[2]
    return answer
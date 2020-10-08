# 23.01
def solution(bridge_length, weight, truck_weights):
    answer = 0
    Q = []
    idx = 0
    load = 0
    while idx < len(truck_weights):
        if load + truck_weights[idx] <= weight:
            Q.append([idx,0])
            load += truck_weights[idx]
            idx += 1
        answer += 1
        for q in Q[::-1]:
            q[1] += 1
            if q[1] == bridge_length:
                Q.remove(q)
                load -= truck_weights[q[0]]
    return answer + bridge_length
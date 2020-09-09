def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        idx = 0
        for c in tree:
            if c in skill:
                if list(skill).index(c) != idx: break
                idx += 1
        else:
            answer += 1
    return answer
# 21:28
from math import *

def solution(w,h):
    if w > h:
        w, h = h, w
    answer = 0
    for i in range(w):
        answer += ceil((i+1)*h/w)-floor(i*h/w)
        if ceil((i+1)*h/w) == (i+1)*h/w:
            answer *= (w//(i+1))
            break
    answer = w*h - answer
    return answer
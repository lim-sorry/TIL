def solution(s):
    numlist = [0]*100001
    string = ''
    for char in s:
        if char.isnumeric():
            string += char
        if char == ',':
            numlist[int(string)] += 1
            string = ''
    numlist[int(string)] += 1
    answer = [0]*max(numlist)
    for i in range(100001):
        if numlist[i] != 0:
            answer[-numlist[i]] = i
    return answer
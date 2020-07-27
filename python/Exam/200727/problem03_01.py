def swap(word):
    result = ''
    for w in word:
        if ord(w) < 97: # 대문자와 소문자를 나누어서 각각 바꿔준다.
            result += chr(ord(w) + 32) # 대문자에서 소문자로 가려면 ord 값의 차이인 32만큼 더하면 된다.
        else:
            result += chr(ord(w) - 32) # 소문자에서 대문자로 가려면 ord 값의 차이인 32만큼 빼주면 된다.
    return result

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(swap('aPpLe'))
    # => 'ApPlE'
    print(swap('SSAFY'))
    # => 'ssafy'
    print(swap('Python'))
    # => 'pYTHON'
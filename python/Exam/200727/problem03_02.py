def caesar(word, n):
    result = ''
    for w in word:
        if ord(w) + n < 91: # 대문자이며 Z를 넘지 않는 경우
            result += chr(ord(w) + n)
        elif ord(w) < 91: # 대문자이며 Z를 넘는 경우 다시 A로 돌아가야한다.
            result += chr(ord(w) + n - 26)
        elif ord(w) + n < 123: # 소문자이며 z를 넘지 않는 경우
            result += chr(ord(w) + n)
        else: # 소문자이며 z를 넘는 경우 다시 a로 돌아가야한다.
            result += chr(ord(w) + n - 26)
    return result

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # => 'fuuqj'
    print(caesar('ssafy', 1))
    # => 'ttbgz'
    print(caesar('Python', 10))
    # => 'Zidryx'
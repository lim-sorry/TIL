def dec_to_bin(n, astr=''): # 5,'' / 2,'1' / 1,'01' / 0,'101'
    bstr = astr # 기존 문자열을 받아온다. 처음에는 공백을 받아온다.
    if n != 0:
        bstr = str(n % 2) + bstr
        bstr = dec_to_bin(n // 2, astr=bstr) # n을 2로 나눈 나머지와 지금까지 문자열을 재귀함수로 불러온다.
    elif bstr == '': # 만약 처음부터 0이 들어오면 0으로 바꿔준다.
        bstr = '0'
    return bstr # n이 0이 될 경우 순차적으로 반환된다.

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(dec_to_bin(10))
    # => '1010'
    print(dec_to_bin(5))
    # => '101'
    print(dec_to_bin(50))
    # => '110010'
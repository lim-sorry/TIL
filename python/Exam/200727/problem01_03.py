import json

def history(movie):
    return True if '과거' in movie['overview'] else False # in을 사용해서 '과거'라는 문자열이 overview안에 포함되어 있는지 검사한다.

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem01_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(history(movie)) 
    # => False
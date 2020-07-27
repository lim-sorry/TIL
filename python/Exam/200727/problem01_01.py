import json

def over(movie):
    return True if movie['user_rating'] >= 8 else False # movie의 'user_rating'을 기준으로 참 거짓을 반환한다.

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem01_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(over(movie)) 
    # => True
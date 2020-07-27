import json

def rotate(data):
    result = {'am':[],'pm':[]}
    for temps in data:
        result['am'].append(temps[0]) # 리스트 속 리스트의 첫째 요소는 am에
        result['pm'].append(temps[1]) # 둘째 요소는 pm에 담아서 반환한다.
    return result

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperature_json = open('problem02_data.json', encoding='UTF8')
    temperature_list = json.load(temperature_json)
    print(rotate(temperature_list))
    # => {
    #     'am': [36.7, 36.9, 37.8, 36.7, 36.3, 36.5, 36.8], 
    #     'pm': [36.5, 37.5, 37.8, 36.5, 36.4, 36.5, 36.6]
    # }

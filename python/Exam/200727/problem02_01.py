import json

def check(data):
    dataset = []
    for temps in data:
        dataset += temps
    for i in range(len(dataset)-2): #연속으로 세 번이기 때문에 뒤에서 세번째까지만 검사한다.
        if dataset[i] >= 37.5:
            if dataset[i+1] >= 37.5:
                if dataset[i+2] >= 37.5:
                    return True # 세 번 모두 37.5 이상이면 True를 반환한다.
    else:
        return False # 모든 검사결과 이상이 없으면 False를 반환한다.

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperature_json = open('problem02_data.json', encoding='UTF8')
    temperature_list = json.load(temperature_json)
    print(check(temperature_list))
    # => True
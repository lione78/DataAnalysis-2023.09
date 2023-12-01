import requests, json, os
import pandas as pd
from urllib.parse import quote

def get_number_of_rent(root_path, tomorrow):
    # api를 파일로부터 가져오는 root
    filename = os.path.join(root_path, 'static/keys/도로명주소apiKey.txt')
    with open(filename) as file:
        road_key = file.read()

    # url 설정
    base_url = 'https://www.juso.go.kr/addrlink/addrLinkApi.do'
    params1 = f'confmKey={road_key}&currentPage=1&countPerPage=10'

    temp = []
    params2 = f'keyword={quote(tomorrow)}&resultType=json'
    url = f'{base_url}?{params1}&{params2}'
    # 전체 url로 결과 값을 가져옮
    result = requests.get(url)
    if result.status_code == 200:
        res = json.loads(result.text)
        temp.append(res['results']['juso'][0]['temp'])
        # {'results' : { 'juso' : [{'roadAddr': X}]}}
    else:
        print(result.status_code)
    # [12일, 13일, 14일], [0, 2, 5] df
    df = pd.DataFrame({'날짜': tomorrow, '온도': temp})

    return df


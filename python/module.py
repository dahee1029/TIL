# 1.모듈: 단일 파이썬 파일(.py), import 사용해서 언제든지 재사용가능
# 2.패키지: 여러 모듈을 포함하는 디렉토리
# 3.라이브러리: 패키지와 모듈의 집합 ex) Pandas, Django

#1.url을 직접 브라우저에 입력=>크롬 확장 프로그램 설치
#   =>JSON Formatter

#2.json 출력 결과를 복사해서 viewer로 확인

import requests
url ="https://random-data-api.com/api/v2/users"
response=requests.get(url).json()
#키를 이용
print(response["address"]["country"])
#get함수를 이용
print(response.get("address").get("country"))
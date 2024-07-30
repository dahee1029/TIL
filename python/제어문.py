#if-else실습

#연도를 입력받아 윤년 판단하기
#윤년이면 'leap year'출력 아니면 'common year'출력

#1. 윤년은 연도가 4로 나누어 떨어지지만 100으로는 나누어 떨어지지 않는다
#2. 윤년은 연도가 400으로 나누어 떨어진다

# year=int(input())

# if year%400==0:
#     print("leap year")
# elif year%100!=0:
#     print("common year")
# elif year%4==0:
#     print("leap year")
# else:
#     print("common year")

# if (year %4 ==0 and year %100!=0) or year %400==0:
#     print("leap year")
# else:
#     print("common year")

#중첩 for문 예제
#정수 n을 입력받아 n단의 왼쪽 직각 이등변삼각형을 그려보세요
#n=5
n=5

#줄의 수
for i in range(n):
    #별의 찍히는 개수
    for i in range(i+1):
        print("*",end="")
    print()

#break
list=[1,2,3,4,5]

#반복문 탈출
for i in list:
    if i ==3:
        break
    print(i) # 1 2 

#반복문 처음으로 돌아가기 
for i in list:
    if i ==3:
        continue
    print(i) # 1 2 4 5 

#testcase, 정수 T 입력 받기
#N X N 행렬, 정수 N을 입력 받기
# 2차원 리스트를 입력 받는다
# ---> 무조건 리스트 컴프리헨션을 써라

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    print(f'{tc} {arr}')
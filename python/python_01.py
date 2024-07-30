'''
a1=1
a2=2.3
a3=2+3
a4='dahee'
a5=[1,2,3]
a6=(1,2,3)
a7=range(1,4)
a8={1,2,3}
a9={"apple":2,"banana":3}
a10=None
a11=lambda x,y: x+y
arr= [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11]
'''
#type나타내기/ eval()
'''
for _ in arr:
    print(type(_))

for i in range(1,12):
    #타입이 str로 나옴
    var=f'a{i}'
    #eval() : 각 타임에 맞게 출력
    var= eval(var)
    print(type(var))
'''

#나누기 중요
'''
9/2=4.5
9//2=4
9%2=1
'''
#불변객체_ (정수나 문자열) 같은 값을 가지면 대부분 같은 메모리주소를 공유
#가변객체_(리스트 등) 같은 값을 가져도 다른 메모리 주소를 가질 수 있다
'''
degree1=36.5
degree2=36.5
list1=[1,2,3]
list2=[1,2,3]
print(id(degree1)) #2603443465200
print(id(degree2)) #2603443465200
print(id(list1)) #2603443390080
print(id(list2)) #2603443415552
'''

#Decimal

from decimal import Decimal
a= Decimal("3.2")-Decimal("3.1")
b= Decimal("3.3")-Decimal("3.2")
#소숫점 셋째자리까지 나타내기
print(f'{a:.3f}') #0.100
print(a==b) #True


#부동소수점
a=3.2-3.1
b=1.2-1.1
#절댓값abs()
print(abs(a-b)) #2.220446049250313e-16

import math
#math.isclose(a,b) :두 숫자가 거의 같은 지 여부를 판단
print(math.isclose(a,b)) #True

num_a=f'{a:.1f}'
num_b=f'{b:.1f}'
print(num_a) #0.1
print(num_b) #0.1


#포멧팅하는 3가지 방법
'''
name=input()
age=int(input())
height=float(input())
#1.포맷코드(옛날방식)
print("저의 이름은 %s이고, 나이는 %d세, 키는 %.2fcm" %(name,age,height))
#2 .format()매서드
print('저의 이름은{}이고, 나이는{}세, 키는{}cm'.format(name,age,height))
#3.f-string
print(f' 저의 이름은 {name}이고, 나이는 {age}세, 키는 {height:.2f}cm')

'''

#미션2. 문자열 parsing
#greeting[start:end:step]
#1. step>0: start 부터 end-1 까지 step만큼 증가
#2. step<0: start 부터 end+1까지 step만큼 감소
#추가내용 
#3. step이 생략되면 기본값은 1
#4. start가 생략되면 기본값은 0

"""
greeting="hello world"

#1.인덱싱->알파벳w를 출력해보세요
print(greeting[6])
#2-1.슬라이싱->hello를 출력해 보세요
print(greeting[:5])
#2-2.슬라이싱->world를 출력해보세요
print(greeting[6:])
#2-3. 슬라이싱->거꾸로 출력해보아요
print(greeting[::-1])
#3. 매서드를 이용하여 문자열의 길이를 출력
print(len(greeting))
"""

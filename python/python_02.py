#int 형변환시 소수점 이하의 값 버림
print(int(3.7)) #3

#알고리즘 풀 때 초기값 설정할 때
#양의 무한대 : float('int')
#음의 무한대 : float('-int')

#문자열 : 불변 시퀀스 자료형
#튜플 : 불변 시퀀스 자료형
my_tuple=(1,)
print(type(my_tuple))
#방향 배열을 하는 경우 튜플을 많이 사용한다
dy=[-1,1,0,0]
dx=[0,0,1,-1]
#상, 하, 좌, 우
directions=[(0,1),(0,-1),(1.0),(-1,0)]
#리스트 : 가변 시퀀스 자료형
'''
#0부터 end-1까지 1씩증가
range(end)
#start부터 end-1까지 1씩 증가
range(start,end)

range(start,end,step)
start<end(증가)
start부터 end-1까지 step만큼 증가(end를 미포함)
start>end(감소)
start부터 end+1까지 step만큼 감소 (end를 미포함)
'''
#딕셔너리 : 불변 비시퀀스 자료형

#예제 중첩된 딕셔너리
my_dict={
    'a1':{'b1':1,"b":2,"b3":3},
    'a2':{'b1':4,"b":5,"b3":6},
    'a3':{'b1':7,"b":8,"b3":9},
}
#value 8을 출력해보세요(2가지 방법)
print(my_dict["a3"]["b"])
value=my_dict.get('a3').get('b2')
print(value)

#세트 : 가변 비시퀀스 자료형 - 중복을 허용하지 않는다 - 집합관 동일한 연산 가능
a={1,2,3,4,5,6}
b={4,5,6,7,8,9}

#합집합
print(a|b)
#교집합
print(a&b)
#차집합
print(a-b)

#로또 번호 만들기
import random
lotto_set=set()
while len(lotto_set)<6:
    number= random.randint(1,45)
    lotto_set.add(number)
lotto_list=list(lotto_set)

print(sorted(lotto_list))


#복사 : 할당, 얕은 복사 , 깊은 복사


#원본이 변경이 될까 안될까? 원본 변경o//메모리 주소 그대로

#할당
list1=[1,2,3,4,5]
list2=list1
list2[0]=5

print(id(list1),list1) #1809338585856 [5, 2, 3, 4, 5]
print(id(list2),list2) #1809338585856 [5, 2, 3, 4, 5]

#얕은 복사, 객체 안에 객체가 있는 경우? 원본변경 o/메모리 주소 달라짐
list1=[1,2,[3,4]]
list2=list1.copy()
list2[2][0]=5

print(id(list1),list1) #1809338638656 [1, 2, [5, 4]]
print(id(list2),list2) #1809338720448 [1, 2, [5, 4]]

#깊은 복사 deepcopy(). 원본이 변경되지 않는다.
import copy
list1=[1,2,[3,4]]
list2=copy.deepcopy(list1)
list2[2][0]=5 

print(id(list1),list1) #1809338720512 [1, 2, [3, 4]]
print(id(list2),list2) #1809338638656 [1, 2, [5, 4]]
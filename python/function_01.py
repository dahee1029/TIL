"""
def get_sum(num1,num2):
    return num1 + num2
num1=5
num2= 2

result=get_sum(num1,num2)

#return이 없는 함수로 변경해 보기
def get_sum(num1,num2):
    result= num1 + num2
    print(result)
num1=5
num2= 2

get_sum(num1,num2)
"""

#내장함수와 메서드의 차이
#내장함수는 별도의 import 없이 사용가능
'''
list1=[]
list2=[1,2,3,4,5]
print("hello")
sum(list2)
print(sum(list2))
'''

#메서드는 class안에 존재
#method는 클래스 내부에 정의된 함수, 객체를 통해 호출
#list.append(), str.upper(), dict.keys()
'''
list1.append(list2)
print(list1)
'''


#재귀함수
#1.자기 자신을 호출
#2.종료 조건이 반드시 있어야 함->무한 호출에 주의
'''
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

result=factorial(5)
print(result)
'''

#LEGB Rule
#1.Built-in scope

"""def outer_function():
    x=1

    def inner_function():
        y=2
        #inner_function에서 x에 접근할 때,
        #우리는 enclosed scope에 접근
        result= x+y
        print(result)
    
    inner_function()

outer_function()"""
'''
a,b,c=1,2,3
def enclosed():
    global a,b,c
    a,b,c=4,5,6

    def local(c):
        print(a,b,c) #4 5 500
    local(500)
    print(a,b,c) #4 5 6
enclosed()
print(a,b,c) #4 5 6
'''

#패킹 언패킹
#패킹 : 여러 값을 하나의 시퀀스로 묶는 과정

# *(애스터리스크)를 패킹 연산자로 활용
numbers=[1,2,3,4,5]
a, *b,c=numbers
print(a) #1
print(b) #[2, 3, 4]
print(c) #5

#print를 이용한 패킹
print("hi","DH","MOO",sep="-") #hi-DH-MOO
print("hi",end=" ") #hi hello
print("hello")

#언패킹
#1. *(애스터리스크)를 언패킹 연산자로 활용!!!알고리즘 output에 종종 활용
names=["DH","MOO","MOND"]
print(*names) #DH MOO MOND
#2. **를 언패킹 연산자로 활용 -> **:딕셔너리 언패킹 연산자
#함수 호출 시 키워드 인자로 전달하는 경우에만 가능
def my_func(x,y,z):
    print(x,y,z)
dict_values={'x':1,'y':2,'z':3}
my_func(**dict_values) #1 2 3

#zip()활용
kr_scores=[10,20,30,50]
math_scores=[20,40,50,70]
en_scores=[40,20,30,50]

for student_scores in zip(kr_scores,math_scores,en_scores):
    print(student_scores)

"""
(10, 20, 40)
(20, 40, 20)
(30, 50, 30)
(50, 70, 50)
"""

#map()함수를 사용하여 numbers의 각 요소의 
#제곱된 값들로 이루어진 새로운 리스트 생성
#lambda 함수사용

numbers=[1,2,3,4,5]
s_numbers=list(map(lambda i: i**2,numbers))
print(*s_numbers)
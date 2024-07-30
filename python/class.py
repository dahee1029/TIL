# class A: pass
# class B(A):pass
# class C(A):pass
# class D(B,C):pass
# print(D.mro())
#어떤 순서로 MRO를 출력할까?
#먼저 D에서 찾는다
#D에 없으면 B에서 찾는다
#B에 없으면 C에서 찾는다
#C에 없으면 A에서 찾는다
#A에도 없으면 object에서 찾는다

#오버라이딩 == 재정의
# 부모클래스에서 정의 메서드를 자식 클래스에서 재정의
# 같은 이름의 메서드를 자식 클래스에서 변경

# class Animal:
#     def speak(self):
#         print('동물소리')
# class Dog(Animal):
#     def speak(self):
#         print('멍멍')
# class Cat(Animal):
#     def speak(self):
#         print('야옹')

# cat=Cat()
# cat.speak()

#스마트폰 다중상속
# class Tool:
#     def __init__(self,name):
#         self.name=name
#     def use(self):
#         print(f'{self.name} 사용')

# class ElectronicDevice:
#     def __init__(self,power):
#         self.power=power
    
#     def turn_on(self):
#         print(f'{self.power}volt 전원 켜기')

# class Smartphone(Tool, ElectronicDevice):
#     def __init__(self,name,power,os):
#         Tool.__init__(self,name)
#         ElectronicDevice.__init__(self,power)
#         self.os=os

#     def run_app(self):
#         print(f'{self.os}에서 앱 실행')

# my_phone=Smartphone("Galaxy",220,"Android")
# my_phone.use()
# my_phone.turn_on()
# my_phone.run_app()

class Parent:
    def __init__(self, age,name,address):
        self.age=age
        self.name=name
        self.address=address

class Child(Parent):
    def __init__(self, age):
        Parent().__init__(age,None,None)

#다중 상속에서는 super를 안쓰는 게 더 좋다=> 유지 보수성 때문
class Smartphone(Tool, ElectronicDevice):
     def __init__(self,name,power,os):
         super.__init__()
         self.name=name
         self.power=power
         self.os=os
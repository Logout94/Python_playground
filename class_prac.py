import os
import sys

class Person:
    # __init__ : 클래스가 생성 될 때 항상 작동하는 함수, 객체에 초기값을 넣거나 어떤 함수의 동작을 필수적으로 해야할 때 사용
    # self : 객체 함수의 첫 인자로 인식하는 클래스 인스턴스 참조형 파라미터로, self 이름 말고 커스텀해서 쓸 수 있다
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Object func : 객체에 포함 된 함수, self 파라미터는 클래스 인스턴스의 참조형 파라미터
    # 인스턴스 :  클래스를 실체화 한 것. ex) 강아지 : 분류, 클래스; 이리온, 이리와: 실체, 구체적 형체
    def myfunc(self):
        print("Hello my name is {} and {} ages ".format(self.name, self.age))

class EmptyClass:
    pass

def main():
    p1 = Person("John", 30)
    p1.myfunc()
    p1.age = 40
    p1.myfunc()
    del p1.age

    try:
        value = p1.age
    except AttributeError:
        print("No value")

if __name__=='__main__':
    main()
import os
import sys

class Person:
    # __init__ : 클래스가 생성 될 때 항상 작동하는 함수, 객체에 초기값을 넣거나 어떤 함수의 동작을 필수적으로 해야할 때 사용
    def __init__(abc, name, age):
        abc.name = name
        abc.age = age
    # Object func : 객체에 포함 된 함수, self 파라미터는 클래스 인스턴스의 참조형 파라미터
    # 인스턴스 :  클래스를 실체화 한 것. ex) 강아지 : 분류, 클래스; 이리온, 이리와: 실체, 구체적 형체
    def myfunc(aaa):
        print("Hello my name is " + aaa.name)

def main():
    p1 = Person("John", 30)
    p1.myfunc()

if __name__=='__main__':
    main()
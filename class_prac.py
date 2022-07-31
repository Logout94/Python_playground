import os
import sys

class Person:
    # __init__ : 클래스가 생성 될 때 항상 작동하는 함수, 객체에 초기값을 넣거나 어떤 함수의 동작을 필수적으로 해야할 때 사용
    def __init__(self, name, age):
        self.name = name
        self.age = age

def main():
    p1 = Person("John", 30)
    print(p1.name)
    print(p1.age)

if __name__=='__main__':
    main()
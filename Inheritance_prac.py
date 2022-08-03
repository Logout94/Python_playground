import os
import sys

# Parent class
class Person:
    def __init__(self, firstname, lastname):
        self.lastname = lastname
        self.firstname = firstname
    
    def printname(self):
        print(self.firstname, self.lastname)
# Child class
class Student(Person):
    def __init__(self, firstname, lastname, year):
        # super(): 부모 클래스의 모든 멤버 변수와 멤버 함수를 가져온다
        super().__init__(firstname, lastname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

def main():
    p1 = Person("John", "Doe")
    p1.printname()

    p2 = Student("Mike", "Olsen", 2019)
    p2.printname()
    p2.welcome()
    
if __name__=='__main__':
    main()
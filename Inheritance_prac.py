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
    pass

def main():
    p1 = Person("John", "Doe")
    p1.printname()

    p2 = Student("Mike", "Olsen")
    p2.printname()

if __name__=='__main__':
    main()
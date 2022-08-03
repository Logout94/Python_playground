import os
import sys

class Person:
    def __init__(self, firstname, lastname):
        self.lastname = lastname
        self.firstname = firstname
    
    def printname(self):
        print(self.firstname, self.lastname)

def main():
    p1 = Person("John", "Doe")
    p1.printname()

if __name__=='__main__':
    main()
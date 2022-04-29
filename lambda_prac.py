import os
import sys

def hap(x, y):
    return x + y

def main():
    #Using function
    print(hap(1, 2))
    #Using lambda
    res = (lambda x, y: x + y)
    print(res(10, 20))

if __name__== '__main__':
    main()
from audioop import reverse
import os
import sys
from functools import reduce
def hap(x, y):
    return x + y

def main():
    #Using function
    print(hap(1, 2))
    #Using lambda
    res = (lambda x, y: x + y)
    print(res(10, 20))

    #Using lambda with map
    a = [1, 2, 3, 4]
    b = [10, 11, 12, 13]
    res2 = list(map(lambda x, y: x+y, a,b))
    print(res2)
    res3 = list(map(lambda x,y: x*y, a,b))
    print(res3)

    #Using lambda with filter
    foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
    res4 = list(filter(lambda x: x%3 == 0, foo))
    print(res4)

    #Using lambda with reduce
    res5 = reduce(lambda x,y: y + x, 'abcdefg')
    print(res5.reverse())
if __name__== '__main__':
    main()
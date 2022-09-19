def main():
    c = Calc()
    print(c.add_val(10, 20))
class Calc:
    def __init__(self):
        self.__a = 0
        self.__b = 0
        self.add_lamda = 0
    # __a : 비공개 변수
    def add_val(self, a, b):
        self.store_val(a, b)
        self.add_lamda = lambda x,y : x+y
        return self.add_lamda(self.__a, self.__b)
    def store_val(self, a, b):
        self.__a = a
        self.__b = b

if __name__=="__main__":
    main()
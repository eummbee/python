#실습1-사칙연산 클래스 만들기
class cal:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def get_add(self):
        return self.__a + self.__b
    
    def get_sub(self):
        return self.__a - self.__b
    
    def get_mul(self):
        return self.__a * self.__b
    
    def get_div(self): #사칙연산에서 0으로 나누는 건 안되기 때문에 오류 설정 해줘야 한다.
        if self.__b == 0:
            return None
        else:
            return self.__a / self.__b

n = cal(4,0)
print(n.get_add())
print(n.get_sub())
print(n.get_mul())
print(n.get_div())
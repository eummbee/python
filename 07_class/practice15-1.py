#실습3-MinLimitCalcalator클래스 만들기
class Calculator():
    def __init__(self):
        self.value = 100

    def sub(self, value):
        self.value -= value

class MinLimitCalcalator(Calculator):

    def sub(self, value):
        self.value = max(value,0) #최소값이 0이 되게 하는 코드
        # self.value = min(value,100)
        self.value -= value
        # self.value = max(0, self.value-value) #이렇게 한 줄로도 짤 수 있다.

    #파이썬은 메소드 오버로딩 안됨 -> C언어는 가능

        
cal = MinLimitCalcalator()
cal.sub(20)
cal.sub(90)
print(cal.value)
    
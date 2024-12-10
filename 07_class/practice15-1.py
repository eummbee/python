#실습3-MinLimitCalcalator클래스 만들기
class Calculator():
    def __init__(self):
        self.value = 100

    def sub(self, value):
        self.value -= value

class MinLimitCalcalator(Calculator):

    def sub(self, value):
        self.value = max(value,0)
        # self.value = min(value,100)
        self.value -= value

        
cal = MinLimitCalcalator()
cal.sub(20)
cal.sub(90)
print(cal.value)
    
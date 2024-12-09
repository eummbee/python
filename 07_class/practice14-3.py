#사번 자동 부여
class Employee:
    serial_num = 1000 #클래스 변수

    def __init__(self, name):
        Employee.serial_num += 1
        self.id = Employee.serial_num
        self.name = name

    def __str__(self):
        return "사번 : {}, 이름 : {}".format(self.id, self.name)
    
e1 = Employee("최사원")
print(e1)

e2 = Employee("안사원")
print(e2)

e3 = Employee("한사원")
print(e3)

employee = [
    Employee('구름'),
    Employee('별'),
    Employee('행성'),
    Employee('달')
]
for i in employee:
    print(i)

#다른방법
print("\n".join(map(str, employee)))
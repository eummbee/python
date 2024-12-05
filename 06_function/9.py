#함수
def f(x):
    return x**2 + 2*x + 1

print(f(3))
print()

#매개변수 없는 함수
def sayHi():
    print("Hi")
    print("Hi")
    print("Hi")
sayHi()
print()

#전역변수, 지역변수
x = 10

def func2():
    print("func2", x)

def func():
    x = 20
    y = 11
    print("func", x, y)

func2() #함수의 지역변수
func()
print(x) #전역변수
#print(y) #지역변수는 밖으로 나올 수 없다.

def func3(x): #x는 지역변수
    print("func3",x) #x는 지역변수
func3(3)
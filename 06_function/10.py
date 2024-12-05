#매개변수로 리스트 전달
def times(a):
    a2 = [i*3 for i in a]
    return set(a2)

v2 = times([1,2,3,4,5])
print(v2)

def sum_mul(a,b):
    sum = a+b
    mul = a*b
    return sum, mul #두개를 return할 수 있다.
s, m = sum_mul(2,3)
print(s,m)
print()

#전역 변수의 유효 범위-global
def oneUp():
    global x #x가 전역 변수임을 표시함
    x = x + 1
    return x
x = 0
print(oneUp())

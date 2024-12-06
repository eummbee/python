#기본 매개변수
def pr_str(txt, count=1, count2=1):
    for i in range(count):
        print(txt)
        print(count2)

pr_str('Hello',3, 2)
pr_str('Hello', 3) #count2변수는 설정된 디폴트 값을 따른다.
print()
pr_str('Hello') #count, count2의 디폴트 값을 따른다.
print()
#pr_str() #txt='12' txt디폴트 값을 정하지 않았기 때문에 error가 발생한다.


#가변 매개변수
def calc_avg(*numbers): #*변수 -> 매개변수가 튜플로 정의된다.
    print(type(numbers))
    sum_v = 0
    for i in numbers:
        sum_v += i
    average = sum_v / len(numbers)
    return average

print(calc_avg(1,2))
print(calc_avg(1,2,3,4,5))

def a():
    return 1,2
print(a())
print(type(a()))
print()


#가변 키워드 매개변수
def introduce(**kwargs): #매개변수는 딕셔너리로 정의 된다.
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f'{key}: {value}')

introduce(name="Alice", age=25, city="New York")


#sorted() 내장함수
list = [2,4,1,4,6]
list.sort() #list자체가 바뀌는 것. 원본을 정렬해 저장한다.
print(list)
list2 = [2,4,1,4,6]
print(sorted(list2)) #sorted()함수 안에 있을때는 정렬해주지만 원본은 변화시키지 않는다.
print(list2) #list2는 그대로이다.


#3번째로 작은 값의 인덱스를 구하라.
#정렬하고 그 값을 원본에서 찾으면 된다.
print(sorted(list2)[2])
print(list2.index(4))

#eval(): 문자열 표현식을 숫자로 변환
print(eval("1+2*2"))

#round() 함수를 쓰지 않고 int를 이용하여 반올림 할 수 있다.
print(int(4.4+0.5))
print(round(4.5)) #banker's rounding 방식을 차용하기 때문에 round(4.5)=5가 나온다.

print(round(2.547)) #소수점 첫째자리에서 반올림
print(round(2.547,1)) #소수점 첫째자리까지
print(round(2.547,2)) #소수점 둘쨰자리까지
print(round(127,-1)) #일의자리 반올림
print(round(127,-2)) #십의자리 반올림
print(round(127))
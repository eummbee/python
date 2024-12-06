#재귀 함수
def hello():
    global count
    
    if count == 3:
        return
    print("Hello")
    count += 1
    hello()

count = 0
hello()

#실습2
#재귀 함수로 피보나치 수 구하기
def fibo(n):
    if n <= 2:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(10))

#시간줄이기 dic에 넣기 -> memoization방법 memory에 저장해서 쓰기 때문에 처리속도가 빠르다.
dic = {1:1,2:1}

def fibo_2(n):
    if n in dic:
        return dic[n]
    dic[n] = fibo_2(n-1) + fibo_2(n-2)
    return dic[n]
print(fibo_2(100))

#리더님 정답 버전
memory = {1:1,2:1}

def fibo_memoization(n):
    if n in memory:
        number = memory[n]
    else:
        number = fibo_memoization(n-1) + fibo_memoization(n-2)
        memory[n] = number
    return number

#람다식
add = lambda x, y: x + y
print(type(add))
print(add(1,2))

def add2(x,y):
    return x+y
print(add(1,2))

#람다 함수를 매개 변수로 전달하기
def call_3(func):
    for i in range(3):
        func()

call_3(lambda:print("hi"))

#다운로드함수
def download(startedCallback, endedCallback):
    startedCallback()
    #download
    print("download 중")
    ###
    ###
    endedCallback()

download(lambda:print("다운로드 시작"), lambda:print("완료되었습니다."))


#lambda-map() 함수와 함께 사용
list(map(int, ["1","2","3"]))

result = map(lambda x:3*x, [1,2,3,4]) #일회용으로 사용할 때 lambda로 함수를 만든다.
print(list(result))


#lambda-filter() 함수와 함께 사용
li = [-5,1,2,-11,76]
value = list(filter(lambda x:x<0, li)) #음수인 것만 필터링
print(value) #[-5, -11]

value = list(filter(lambda x:x>10, li)) #x>10인 것만 필터링
print(value) #[76]

#2배 후 3이상인것만 출력
print(list(filter(lambda x: x >= 3, map(lambda x: x*2,li))))

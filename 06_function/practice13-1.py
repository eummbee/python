#https://school.programmers.co.kr/learn/courses/30/lessons/12910?language=python3
#프로그래머스 문제 1
def solution(arr, divisor):
    answer=[]
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            answer.sort()
    if len(answer) == 0:
        answer.append(-1)
    return answer
print(solution([3,2,6],10))

###1-짧은풀이
def solution(arr, divisor):
    arr = [x for x in arr if x % divisor == 0]
    arr.sort()
    return arr if len(arr) !=0 else [-1]


#https://school.programmers.co.kr/learn/courses/30/lessons/68644?language=python3
#프로그래머스 문제2
def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
            for j in range(i+1,len(numbers)): 
                a = numbers[i] + numbers[j]
                if a not in answer:
                    answer.append(a)
    answer.sort()
    return answer
print(solution([5,0,2,7]))

###2-짧은풀이
def solution_2(numbers):
    answer = set()
    for i in range(len(numbers)-1):
            for j in range(i+1,len(numbers)): 
                answer.add(numbers[i] + numbers[j])
    return sorted(answer) #set은 중복을 허용하지 않기 때문에 중복제거를 위해 사용한다. sorted는 리스트로 반환해주기 때문에 list()를 쓰지 않아도 된다.
print(solution_2([5,0,2,7]))


#https://school.programmers.co.kr/learn/courses/30/lessons/12947?language=python3
#프로그래머스 문제3
def solution(x):
    answer = True
    s=0
    l = list(map(int, list(str(x))))
    for i in l:
        s = s + i
    if x%s==0:
        return answer
    else:
        answer = False
    return answer
print(solution(11))

###3-짧은 풀이
def Harshad(n):
    return n%sum(int(x) for x in str(n)) == 0
print(Harshad(11))

###리더님 버전
def solution(x):
    s = str(x) #str은 문자열 리스트이다.
    sum = 0
    for i in s:
        sum += int(i)

    return x % sum == 0


#https://school.programmers.co.kr/learn/courses/30/lessons/12917?language=python3
#프로그래머스 문제4
def solution(s):
    answer = ''
    answer = list(s)
    answer.sort()
    answer.reverse()
    return "".join(answer)
print(solution("Zbcdefg"))

###4-짧은 풀이
def solution(s):
    return ''.join(sorted(s,reverse=True)) #문자열은 1차원 리스트 이다.
print(solution("Zbcdefg"))


#https://school.programmers.co.kr/learn/courses/30/lessons/176963
#프로그래머스 문제5
def solution(name, yearning, photo):
    answer=[]
    for i in range(len(photo)):
        s=[]
        for j in range(len(photo[i])):
            if name.count(photo[i][j]) == 1:
                s.append(yearning[name.index(photo[i][j])])
            else:
                s.append(0)
        answer.append(sum(x for x in s))
        
    return answer

#5-dictionary 버전
def solution(name, yearning, photo):
    answer = []
    dict1 = {}
    for i in range(len(name)):
        dict1[name[i]] = yearning[i]
    
    for x in range(len(photo)):
        result = 0
        for y in range(len(photo[x])):
            if name.count(photo[x][y]) == 1:
                result += dict1[photo[x][y]]
        answer.append(result)
    return answer

#리더님 버전
def solution(name, yearning, photo):
    answer = []
    d = {}
    for i in range(len(name)):
        d[name[i]] = yearning[i]
    
    for i in photo:
        sum = 0
        for j in i:
            v = d.get(j)
            if v:
                sum += v
        answer.append(sum)
    return answer

#zip함수
a = [1,2,3,4]
b = ["a","b","c","d"]
c = list(zip(a,b)) #튜플로 묶어서 리스트로 반환
print(c)
d = dict(zip(a,b)) #딕셔너리로 만들기
print(d)


#https://school.programmers.co.kr/learn/courses/30/lessons/147355?language=python3
#프로그래머스 문제6
def solution(t,p):
    answer = 0
    n = len(t)-len(p)+1
    for i in range(n):
        if t[i:i+len(p)] <= p: #길이가 똑같다는 가정이 있기 때문에 이것이 가능하다.
            answer += 1
    return answer
print(solution("3141592","271"))


#https://school.programmers.co.kr/learn/courses/30/lessons/181919
#프로그래머스 문제7-콜라츠 수열
def solution(n):
    answer=[]
    answer.append(n)
    while n>1:
        if n%2==0:
            n = n/2
        else:
            n = 3*n+1
        answer.append(n)
    return answer
print(solution(6))

##7-재귀함수 버전
answer=[]

def solution(n):
    if n==1:
        answer.append(n)

    elif n%2==0:
        answer.append(n)
        solution(n/2) #재귀함수로 인해 다시 함수가 반복되기 때문에 answer=[]리스트는 함수 바깥에서 정의해야한다.
        
    else:
        answer.append(n)
        solution(n*3+1)
        
    return answer
            
print(solution(10))



    



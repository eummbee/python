#2024-12-03 반복문 수업
i=0
while i<5:
    i+=1
    print(i)
print("끝")

#1~10중에 홀수만 출력
num = 0
while num < 10:
    num+=1
    if num%2!=1:
        continue
    print(num)

# 실습1
#1부터 사용자가 입력한 수까지 정수의 합 계산
num = 0
a = int(input("어디까지 계산할까요?"))
for i in range(1, a+1):
    num+=i
print(num)

#홀수의 합만 구하기
num = 0
a = int(input("어디까지 계산할까요?"))
for i in range(1, a+1):
    if i%2==1:
        num+=i
print(num)
print()

#실습2
#입력한 숫자만큼 카운트하고 "발사" 출력
a = int(input("몇 초?: "))
for i in range(a,0,-1):
    print(i,end=" ")
print("발사!!")
print()

#실습3
#구구단 만들기-사용자가 입력한 숫자의 구구단 출력
a = int(input("몇 단을 출력할까요? "))
for i in range(1,10):
    print(f"{a} * {i} = {a*i}")

#리스트내포
a = [1,2,3,4,5]
a3=[]
a4=[]

a3 = [i*3 for i in a]
print(a3)

a4 = [i*3 for i in a if i%2==0]
print(a4)

#이중 for문
for y in range(3):
    for x in range(2):
        print(f"y: {y}, x: {x}")
    print()

#구구단 전체
for i in range(2,10):
    print(f'[{i} 단]')
    for j in range(1,10):
        print(f'{i} x {j} = {i*j}')
    print()
    
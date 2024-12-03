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
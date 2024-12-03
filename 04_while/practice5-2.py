#1번
a = int(input("몇 줄? >"))
for i in range(1,a+1):
    for j in range(1,i+1):
        print('*', end="")
    print()

#2번
sum = "*"
a = int(input("몇 줄? >"))
for i in range(1,a+1):
    for j in range(a-i,0,-1):
        print(" ", end="")
    print(sum*i)

#3번
sum = "*"
a = int(input("몇 줄? >"))
for i in range(1,a+1):
    for j in range(a-i,0,-1):
        print(" ", end="")
    print(sum*i,sum*(i-1),sep="")

#간단한 버전
a = int(input("몇 줄? > "))
for i in range(1,a+1):
    print(" "*(a-i)+"*"*(2*i-1))
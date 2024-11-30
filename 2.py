#변수 배우기
ive = "장원영"
print(ive)
print(f"나는 {ive}입니다.") #f문자열 포매팅 {}에 변수를 넣을 수 있다. +- 같은 포현식도 가능.
print("나는 ", ive, "입니다.",sep="")
print("나는 " + ive + "입니다.")

a = 7
print(type(a))
a=7.2
print(type(a))
a = "ive"
print(type(a))

print("111'111")

#진수표현하기
num = 10
b_num = 0b1010
h_num = 0xA

print(num)
print(b_num)
print(h_num)

print(bin(10))
print(hex(10),"\n")

#아스키 코드값과 문자
print(ord('0'))
print(ord('A'))
print(chr(48))
print(chr(65), "\n")

# 연산자
print(3 // 2)
print(3.25 // 2)
print(3 % 2)
print(3.25 % 2)
print(2**3)
print(2**10, "\n")

#실습문제-몫과 나머지 계산하기
print("빵의 개수 : ", 30//4)
print("남은 빵의 개수 : ", 30%4, "\n")

#문자열 연산
print("장원영"+" 럭키비키")
print("럭키"*10, "\n")
#print("럭키"*"비키") -> error!

#input 입력함수
song = input("너의 최애 노래는? ")
print(song)
print(type(song), "\n") #input으로 받은 값은 문자열(str)

#형변환
a = input("1+1= ")
#print(a)
print(int(a)*2)

number = int(input()) #입력받은걸 바로 형변환 가능
print(type(number))

a = 2
print(str(2)*10)
print(str(2)+"입니다")
#print(2+"입니다") - > error! 문자열끼리만 '+'로 이을 수 있다.


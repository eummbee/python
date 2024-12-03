#문자열 함수
print("오늘은 12월 %d일 입니다." % 2)
print("오늘은 %d월 %d일 입니다." % (12,2))
print("오늘은 %d%s %d일 입니다." % (12, '월', 2))
print(f"오늘은 {12}{'월'} {2}일 입니다.")
print("오늘은 " + str(12) + "월 " + str(2) + "일 입니다.")
print("오늘은 ", 12, "월 ", 2, "일 입니다.", sep="")
print()

print("Hello".upper()) #대문자로 바꾸기
print("Hello".lower()) #소문자로 바꾸기
print()

#split 문자열을 특정문자를 기준으로 나눠서 리스트로 반환
friends = "고찬국 김다운 김민창"
a = friends.split() #기본이 " "
print(a)

sentence = "{}월 {}일".format(12,2)
print(sentence)

b = "   111   222   "
print(b.replace("111", "222"))
print(b.strip()) #앞 뒤 공백 제거 (왼쪽만:lstrip, 오른쪽만:rstrip)
print(b.split())

#조건문
print(1==2)

x = 3
print(1 < x < 5) #C언어는 print(x>1 && x<5)

#C언어와 다르게 파이썬은 and, or, not을 적어야함.
print(True and False)
print(True or False)
print(not True)
print(not False)
print()

#in연산자
cart = ["계란", "마늘", "콩나물", "커피"]
print("두부" in cart)
print("계란" in cart)
print()

#조건문
if 1 > 3:
    print("True")
    print("True")
print("False")
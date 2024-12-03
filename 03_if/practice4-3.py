#점수를 입력 받아 등급 나누기
a = int(input("점수를 입력해 주세요: "))
if a<=100:
    if a>=90:
        print("A")
    elif a>=80:
        print("B")
    elif a>=70:
        print("C")
    elif a>=60:
        print("D")
    else:
        print("E")
else:
    print("만점은 100점 입니다.")


#효율적인 코드 ('>=' 보다 '>' 이것이 더 처리속도가 빠르다.)
a = int(input("점수를 입력해 주세요: "))
if a < 60:
    print("E")
elif a < 70:
    print("D")
elif a < 80:
    print("C")
elif a < 90:
    print("B")
else:
    print("A")

if a > 100:
    print("만점은 100점 입니다.")
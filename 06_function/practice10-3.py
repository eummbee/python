#실습5. 1~30까지의 자연수 중 배수와 배수의 개수를 계산하는 함수를 정의하시오.
def get_times(n):
    global count #전역변수 count

    for i in range(1,31):
        if i % n == 0:
            print(i, end=" ")
            count += 1 #count = ~ 으로 선언한 것이기 때문에 global을 붙여 전역변수로 만든다음 count를 선언해야한다.         

count = 0 #global 이 없을 시 여기 count는 전역변수이고 함수 안에 count는 지역변수 이므로 둘은 다른 변수가 되어버린다.
n = 3
get_times(n)
print(f"\n{n}의 배수의 개수: {count}")



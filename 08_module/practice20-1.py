import random
import time

word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple', 'grape', 'garlic', 'onion', 'potato']

n = 1 #문제번호

input("[타자 게임] 준비되면 엔터!")
start = time.time() #시작 시간

while n < 11:
    print("문제", n)
    question = random.choice(word) #choice는 중복이 나온다.
    print(question) #문제출제
    user = input()
    if question == user:
        print("통과!!")
        n += 1 #다음 문제 카운트
    else:
        print("오타! 다시 도전!")
    
end = time.time() #종료 시간
et = end - start
print(f'타자 시간: {et: .2f}초') #.2f 실수를 소수점 둘째자리까지 표시
      
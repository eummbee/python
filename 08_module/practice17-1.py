import random

com = random.randint(1, 100)
min_v = 1
max_v = 100
count = 0
score = 100

while count < 10:
    try:
        count += 1
        guess = int(input(f"숫자 입력([{count}회]%d ~ %d): " % (min_v, max_v)))

        if guess < 0 or guess > 100:
            print("입력 범위를 초과했어요")
        elif com == guess:
            print("정답이에요!!")
            print(f"정답 : {com}")
            print(f"점수 : {score}")
            break
        elif com > guess:
            print("랜덤수보다 작아요")
            min_v = guess
        else:
            print("랜덤수보다 커요")
            max_v = guess
        score -= 10
    except ValueError:
        print("숫자만 입력 가능합니다.")

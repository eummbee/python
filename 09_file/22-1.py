import random
import time

try:
    with open("word.txt", 'r') as f: #word.txt 파일 읽어서 리스트로 반환
        word = f.read().split()

    n = 1
    
    input("[타자 게임] 준비되면 엔터!")
    start = time.time()

    while n < 11:
        
        print("문제", n)
        question = random.choice(word)
        print(question)
        user = input()

        if question == user:
            print("통과!!")
            n += 1
        else:
            print("오타!! 다시 도전")
    end = time.time()
    print(f'게임 소요 시간 : {end-start:.2f}초')

except:
    print("파일을 찾을 수 없습니다.")



##다른방법
# if os.path.exists("word.txt"): #해당 파일이 있으면 아래를 열어라
#     with open("word.txt", 'r') as f:
#         word = f.read().split()

# else : #없으면 다음과 같다.
#     word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
#         'grape', 'garlic', 'onion', 'potato']
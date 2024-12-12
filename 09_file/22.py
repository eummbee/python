import random

with open("word.txt", 'w') as f: #word.txt 파일 만들어서 word 리스트 넣기
    word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple', 'grape', 'garlic', 'onion', 'potato']
    for i in word:
        f.write(i + ' ')

with open("word.txt", 'r') as f:
    data = f.read().split()
    #data = f.readlines() #\n인 경우에 이렇게도 가능
    word = random.choice(data)
    print(data)
    print(word)
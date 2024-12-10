#실습-로또 번호 뽑기
import random
lotto = []

while len(lotto)<6:
    num = random.randint(1,45)
    lotto.append(num)
    if lotto.count(num)>1:
        lotto.remove(num)
                
lotto.sort()
print(lotto)

#다른 버전
lotto = []

#set()버전

#random.sample(range(1,46),6)
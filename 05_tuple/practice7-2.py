#실습2. 딕셔너리 사용
score = dict()
score['Alice'] = 85
score['Bob'] = 90
score['Charlie'] = 95

score['David'] = 80
score['Alice'] = 88

del(score['Bob']) #삭제
#a = dict.pop('Bob') #del과 차이점은 'Bob'의 값이 반환이 된다는 것이다.

for i in score.keys():
    print(i,score.get(i))
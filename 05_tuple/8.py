#2차원 리스트
d = [
    [10,20],
    [30,40],
    [50,60]
]

print(d)
print(d[0][0])
print(d[1][1])
d.append([70,80])
print(d)
d[0][0] = 90
print(d)

# d[1].pop() #d[1]에 마지막열 삭제하기
print(d)
print()

#list 값 출력하기
for i in range(0,len(d)):
    for j in range(0,len(d[i])):
        print(d[i][j], end=" ")
    print()
print()

#리스트 값 출력하기(열의 크기가 같을 때는 이 방법 사용)
for x, y in d:
    print(x,y)

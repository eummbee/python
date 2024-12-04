#튜플 생성
t1 = (10, 20, 30)
print(type(t1))
print(t1)
print(t1[0])
##del t1[0] ->특정 요소 삭제 안됨.
##t1[0] = 3 안됨
print()

#튜플 삭제
del (t1)

t1 = (10)
t3 = (10, )
t4 = 10,

#셋(set)
set1 = {1,2,3,3} #중복된 문자는 한번만 저장한다.
set2 = set([1,2,3,4])
print(set1) 
print(set2)
set2.add(4)
print(set2)
while len(set2) > 0:
    a = set2.pop()
    print(a)
print()

l1 = [1,2,3,4]
while len(l1) > 0:
    a = l1.pop()
    print(a)
print()

set3 = set("appple")
print(set3)
while len(set3) > 0:
    a = set3.pop()
    print(a)

#for루프 이용해서 중복 제거하기
name = ["1","2","3","2"]
a = []
for i in range(len(name)):
    if a.count(name[i]) < 1:
        a.append(name[i])
name = a
print(name)
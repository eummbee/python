#실습1. set 사용 #####틀린버전 ##m쪽은 중복이 나올 수 있기 때문에 set으로 넣으면 안된다.
# n, m = map(int,input().split())
# set1 = set()
# set2 = set()
# for i in range(n):
#     s = input()
#     set1.add(s)

# for j in range(m):
#     ss = input()
#     set2.add(ss)

# answer = set1 & set2
# print(len(answer))

#set사용
n, m = map(int, input().split())
s = set()
for i in range(n):
    data = input()
    s.add(data)

count = 0

for j in range(m):
    data = input()
    if data in s:
        count+=1
print(count)

#list사용
n, m = map(int, input().split())
s = []
for i in range(n):
    data = input()
    s.append(data)

count = 0

for j in range(m):
    data = input()
    if data in s:
        count+=1
print(count)

#dictionary 사용
n, m = map(int, input().split())
s = dict()
for i in range(n):
    data = input()
    s[data] = True #dictionary[key]=value

count = 0

for j in range(m):
    data = input()
    if data in s:
        count+=1
print(count)


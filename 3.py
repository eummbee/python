a = []
b = [1,2,3,4]
c = ["장원영", "안유진", "이서", "리즈", "레이", "가을"]
d = [1, "아이브"]


print(len(c)) #리스트 요소의 개수
print(c[0]) #n번째 요소
print(c[1])
c[0] = "카리나"
print(c)
del c[0] #리스트 요소 삭제
print(c)
c.append("baddie")
print(c)

print(b[-1]) #뒤에서 첫번째
print(b[-2])
print(type(b))

#리스트 슬라이싱
seasons = ["봄", "여름", "가을", "겨울"]
print(seasons[0:1])
print(seasons[0:2])
print(seasons[:2])
print(seasons[1:])
print(seasons[2:])
print(seasons[1:3])
print(seasons[::2])
print(seasons[::-1]) #리스트 요소 순서 반전해서 출력

seasons2 = ["봄", "여름", "가을", "겨울", [1,2,3,4]] #리스트 안에 리스트 가능
print(seasons2[-1][0])

abcd = "abcd"
abc = ['a','b','c','d']
print(len(abcd))
print(len(abc))
print()

#a를 이용해서 짝수만 뽑은 리스트 만들기
a = [1,2,3,4,5,6,7,8,9,10]
even = a[1::2]
print(even)

#sort 정렬
a = [3,4,2,1]
a.sort()
print(a)

b = ["a", "c", "b", "d"]
b.sort()
print(b)

c = ["1", "2", "10", "11"] #문자는 숫자랑 정렬이 다르다.
c.sort()
print(c)

d = ["강남", "강북", "서","서","서"]
#d.reverse() #순서 반전
print(d)
print(d.index("서"))
first = d.index("서")+1
print(first + d[first:].index("서")) #두번째 "서" 찾기
print(d.count("서"))

#index, pop, count
e = [1,2,3,4,5,6,6,6]
e.pop() #리스트 제일 마지막 요소 지우기
print(e)
print(e.index(2)) #특정 위치 요소 찾기
print(e.count(6)) #같은 요소 갯수

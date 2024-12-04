#딕셔너리
a = {}
print(type(a))
b = {1}
print(type(b))
c = dict()
c = {1:'a', 'b':'b'}
print(c)
c[2] = 'c'
c['c'] = 2
print(c)
del c[2]
del c['b']
print(c)
print()

for i in c.keys():
    print(i, c.get(i))

print(1 in c)
print()

###############################
dic = {
    "비트": "0이나 1의 값을 가지는 컴퓨터 데이터의 최소 단위",
    "변수": "어떤 1개의 자료를 저장하기 위한 메모리 할당 공간",
    "리스트": "여러 개의 연속적인 자료를 저장하는 자료구조"
}


print("★ 컴퓨터 사전 ★")
word = input("검색할 단어를 입력하세요: ")
if word in dic:
    print(f'{word}: {dic[word]}')
else:
    print("정의된 단어가 없습니다.")



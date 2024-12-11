f = open("text.txt", "w") #파일에 데이터를 쓰기 위해서 연다. 기존파일을 초기화한다.
f.write("Hi\n")
f.close()

f2 = open("text.txt")
print(f2.read())
f2.close()

f = open("text.txt", "a") #파일 뒤에다가 추가한다.
f.write("Hi22\n")
f.close()

f2 = open("text.txt")
print(f2.readline(), end="") #파일의 한줄씩 읽기
print(f2.readline(), end="") #그 다음의 한줄 읽기
f2.close()

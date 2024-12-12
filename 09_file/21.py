# f = open("text.txt", "w") #파일에 데이터를 쓰기 위해서 연다. 기존파일을 초기화한다.
# f.write("Hi\n")
# f.close()

# f2 = open("text.txt")
# print(f2.read())
# f2.close()

# f = open("text.txt", "a") #파일 뒤에다가 추가한다.
# f.write("Hi22\n")
# f.close()

# f2 = open("text.txt")
# print(f2.readline(), end="") #파일의 한줄씩 읽기
# print(f2.readline(), end="") #그 다음의 한줄 읽기
# f2.close()

# f4 = open("text.txt")
# print(f4.readlines()) #파일의 모든 줄을 읽고 각 줄을 리스트의 요소로 반환
# f4.close()

# f = open("text.txt", "w") 
# f.write("Hi\n")
# f.close()

# f5 = open("text.txt", "r+")
# print(f5.read())
# print(f5.tell())
# f5.seek(0)
# print(f5.write("8"))
# f5.close()

# f6 = open("text.txt", "r+")
# str6 = f6.read()
# print(f6.tell())
# f6.seek(str6.find('5')) #'5'커서 찾아라
# print(f6.write("87")) #바꾼 갯수
# f6.close()

with open("text.txt", "r+") as f7: #close()를 안해도됨.
    str6 = f7.read()
    print(f7.tell())
    f7.seek(str6.find('2')) #'5'커서 찾아라
    print(f7.write("8")) #바꾼 갯수
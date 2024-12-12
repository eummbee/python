with open("member.txt", 'w', encoding="UTF-8") as f: #텍스트 파일에 한글깨짐이 발생하여 'encoding'옵션을 추가하였다.
    for i in range(3):
        name = input('이름 비밀번호 : ')
        f.write(name + '\n')

with open("member.txt", 'r', encoding="UTF-8") as f1:
    data = f1.read()
    print(data)
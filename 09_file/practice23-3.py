name = input("이름을 입력하세요. ")
password = input("비밀번호를 입력하세요. ")

dic = {}
with open("member.txt", 'r', encoding="UTF-8") as f:
    for i in f:
        n, p = i.split()
        dic[n] = p

    if password == dic.get(name):
        print("로그인 성공")
        number = input("전화번호를 입력하세요. ")
    else:
        print("로그인 실패")

#기존정보를 저장하는 리스트 만들기
with open("member.txt", 'r', encoding="UTF-8") as f:
    m_tel_list  = f.readlines()
    print(m_tel_list)

user_tel = name + " " + number + "\n"

#이름이 맞으면 번호 바꾸고, 이름이 틀리면 기존꺼 그대로
dict = {}
with open("member_tel.txt", 'w', encoding="UTF-8") as f1:
    write = False
    for i in m_tel_list:
        if i.split()[0] == name:
            f.write(user_tel)
            write = True
        else:
            f.write(i)

    if not write:
        print("not write", user_tel)
        f.write(user_tel)





    # for i in f1:
    #     na, nu = i.split()

    # if na == name:
    #     nu == number
    #     f1.write(name + " " + number + "\n")
    # else:
    #     f1.write(name + " " + number + "\n")


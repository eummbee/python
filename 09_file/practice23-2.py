name = input("이름을 입력하세요. ")
password = input("비밀번호를 입력하세요. ")

with open("member.txt", 'r', encoding="UTF-8") as f:
    check = f.read().split("\n")
    np = name + " " + password

    if np in check:
        print("로그인 성공")
    else:
        print("로그인 실패")


## 다른 방법
with open("member.txt", 'r', encoding="UTF-8") as f:
    for i in f:
        n, p = i.split()

        if n == name and p == password:
            print("로그인 성공")
            break
        else:
            print("로그인 실패")
            break


###다른 방법(dictionary): for루프 돌지 않고 수가 많을 때 빠르게 찾는 방법
dic = {}
with open("member.txt", 'r', encoding="UTF-8") as f:
    for i in f:
        n, p = i.split()
        dic[n] = p

    if password == dic.get(name):
        print("로그인 성공")
    else:
        print("로그인 실패")

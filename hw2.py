#과제2. 자판기 프로그램
print("================= RESTART")
vending_macine = ['게토레이', '레쓰비', '생수', '이프로']
a = input("마시고 싶은 음료? ")
if (a in vending_macine) == True:
    print(f"{a} 드릴게요")
else:
    print(f"{a}는 지금 없네요")

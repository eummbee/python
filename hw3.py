#과제2에서 만든 자판기 프로그램 응용
vending_machine = ['게토레이','게토레이','레쓰비','레쓰비','생수','생수','생수','이프로']
print(f"남은 음료수: {vending_machine}\n")

a = input("사용자 종류를 입력하세요:\n1.소비자\n2.주인\n")

if a == "1" or a == "소비자":
    drink1 = input("마시고 싶은 음료? ")

    if vending_machine.count(drink1) != 0:
        print(f"{drink1} 드릴게요")
        vending_machine.remove(drink1)
        print(f"남은 음료수: {vending_machine}\n")
    else:
        print(f"{drink1}는 지금 없네요")

elif a == "2" or a == "주인":
    b = input("할 일 선택:\n1.추가\n2.삭제\n")
    print(f"남은 음료수: {vending_machine}\n")

    if b == "1" or b == "추가":
        add = input("추가할 음료수? ")

        if vending_machine.count(add) != 0: 
            vending_machine.insert(vending_machine.index(add),add)
            print("추가 완료")
            print(f"남은 음료수: {vending_machine}")
        else:
            vending_machine.append(add)
            print("추가 완료")
            print(f"남은 음료수: {vending_machine}")


    elif b == "2" or b == "삭제":
        remove = input("삭제할 음료수? ")

        if vending_machine.count(remove) != 0:
            vending_machine.remove(remove)
            print("삭제 완료")
            print(f"남은 음료수: {vending_machine}")
        else:
            print(f"{remove}는 지금 없네요")

    else:
        print("잘못된 값")

else:
    print("잘못된 값")

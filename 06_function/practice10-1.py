#실습3. 자판기 프로그램 함수화
#hw3에서 한 자판기 프로그램을 함수화 해보기.

#남은 음료수를 확인하는 함수
def check_machine(): 
    print(f"남은 음료수: {vending_machine}\n")

#음료수가 있는지 확인하는 함수
def is_drink(): 
    if drink1 in vending_machine:
        print(f"{drink1} 드릴게요")
        vending_machine.remove(drink1)
    else:
        print(f"{drink1}는 지금 없네요")

#음료수를 추가하는 함수
def add_drink(): 
    add = input("추가할 음료수? ")

    if add in vending_machine: 
        vending_machine.insert(vending_machine.index(add),add)
        print("추가 완료")
    else:
        vending_machine.append(add)
        print("추가 완료")

#음료수를 제거하는 함수
def remove_drink(): 
    remove = input("삭제할 음료수? ")

    if remove in vending_machine:
        vending_machine.remove(remove)
        print("삭제 완료")

    else:
        print(f"{remove}는 지금 없네요")

#자판기 리스트
vending_machine = ['게토레이','게토레이','레쓰비','레쓰비','생수','생수','생수','이프로']
check_machine()

a = input("사용자 종류를 입력하세요:\n1.소비자\n2.주인\n")

if a == "1" or a == "소비자":
    drink1 = input("마시고 싶은 음료? ")
    is_drink()
    check_machine()

elif a == "2" or a == "주인":
    b = input("할 일 선택:\n1.추가\n2.삭제\n")
    check_machine()

    if b == "1" or b == "추가":
        add_drink()
        check_machine()

    elif b == "2" or b == "삭제":
        remove_drink()
        check_machine()

    else:
        print("잘못된 값")

else:
    print("잘못된 값")


#################################################################
######정답 버전
vending_machine = ['게토레이', '게토레이', '레쓰비', '생수', '이프로']

def check_machine():
    print("남은 음료수: ", vending_machine)

def is_drink(vending_machine, drink):
    return drink in vending_machine

def add_drink(vending_machine, drink):
    vending_machine.append(drink)
    vending_machine.sort()

def remove_drink(vending_machine, drink):
    vending_machine.remove(drink)

while(1):
    who = int(input("사용자 종류를 입력하세요(1.소비자, 2.주인) : "))
    if who == 1:
        drink = input("마시고 싶은 음료? ")
        if is_drink(vending_machine, drink):
            print(drink, "드릴게요")
            remove_drink(vending_machine, drink)
            check_machine()
        else:
            print(f"{drink}는 지금 없네요")
    else:
        todo = int(input("할 일 선택(1.추가, 2.삭제) : "))
        if todo == 1:
            print("남은 음료수: ", vending_machine)
            drink = input("추가할 음료수? ")
            add_drink(vending_machine, drink)
            print("추가 완료")
            print("남은 음료수: ", vending_machine)
        else:
            print("남은 음료수: ", vending_machine)
            drink = input("삭제할 음료수? ")
            if is_drink(vending_machine, drink):
                remove_drink(vending_machine, drink)
                print("삭제 완료")
                print("남은 음료수: ", vending_machine)
            else:
                print(f"{drink}는 지금 없네요")

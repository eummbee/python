#실습1
def func(x,y):
    if x == y:
        print(f"결과(곱): {x*y}")
    else:
        print(f"결과(합): {x+y}")
func(2,2)
func(2,3)
print()

#실습2
def ship(가격,수량):
    if 가격*수량 < 20000:
        return 가격*수량 + 2500
    else:
        return 가격*수량
total = ship(30000,2)
print(f"상품1 가격: {total}")
total = ship(17500,2)
print(f"상품2 가격: {total}")

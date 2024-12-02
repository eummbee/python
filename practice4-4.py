#교통비를 낼 때 나이와 결제 방법에 따른 금액을 출력하세요.
age = int(input("나이를 입력해 주세요: "))
pay = input("결제 방법을 입력해주세요. ('카드' 또는 '현금'만 입력): ")

if pay == "카드":
    if age < 8:
        print(f"{age}세의 {pay} 요금은 무료 입니다.")
    elif age < 14:
        print(f"{age}세의 {pay} 요금은 450원 입니다.")
    elif age < 20:
        print(f"{age}세의 {pay} 요금은 720원 입니다.")
    elif age < 75:
        print(f"{age}세의 {pay} 요금은 1200원 입니다.")
    else:
        print(f"{age}세의 {pay} 요금은 무료 입니다.")
elif pay == "현금":
    if age < 8:
        print(f"{age}세의 {pay} 요금은 무료 입니다.")
    elif age < 14:
        print(f"{age}세의 {pay} 요금은 450원 입니다.")
    elif age < 20:
        print(f"{age}세의 {pay} 요금은 1000원 입니다.")
    elif age < 75:
        print(f"{age}세의 {pay} 요금은 1300원 입니다.")
    else:
        print(f"{age}세의 {pay} 요금은 무료 입니다.")
else:
    print("'카드' 또는 '현금'만 입력해주세요.")

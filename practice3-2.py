#실습3

#1번
name = input("이름을 입력하세요.")
age = input("나이를 입력하세요.")
print(f"안녕하세요! {name}님 ({age}세)")
print()

#2번
name = input("이름을 입력하세요.")
birth = int(input("태어난 년도를 입력하세요."))
year = int(input("올해 년도를 입력하세요."))
print(f"올해는{year}년,{name}님의 나이는{year-birth+1}세 입니다.")
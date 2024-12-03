#실습5
#리스트 평균 구하기
a = input("숫자 여러 개 입력 > ")
aa = a.split(" ")
aa = list(map(int, aa)) #aa=[int(i) for i in aa] -> 이렇게 map()을 쓰지않고 리스트 내포 for문을 이용해서 리스트의 요소들을 int형으로 변환시킬 수 있다.
print(aa)
b = max(aa)
c = min(aa)
print(f"가장 큰 값: {b}")
print(f"가장 작은 값: {c}")

aa.remove(b)
aa.remove(c)
print(f"나머지 값의 평균: {sum(aa)/len(aa)}")



###################################################
#정답 버전
# 1
input_nums = input('숫자 여러개 입력 > ').split()
numbers = []
for n in input_nums:
    numbers.append(int(n))
print(numbers)

# 최대값
# 1 리스트 평균 구하기
max_val = numbers[0] #첫번째 값을 최대값으로 설정함
for i in numbers:  
    if i > max_val:  # i(요소값)이 max_val 보다 크면
        max_val = i  # max_val에 i값 저장
        
# 2 가장 큰/작은 값 구하기
max_val = max(numbers) # max() 사용
print("가장 큰 값:", max_val)

min_val = min(numbers) # max() 사용
print("가장 작은 값:", min_val)

# 3 나머지 값의 평균 구하기
numbers.remove(max_val)
numbers.remove(min_val)
# 평균 = 합계 / 개수
avg = sum(numbers) / len(numbers)
print("나머지 값의 평균: ", avg)
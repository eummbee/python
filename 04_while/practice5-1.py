print('*** 자리배치도 ***')
customer = int(input('고객수 입력: '))
row = int(input('좌석행 수 입력: '))

if customer % row == 0:
    column = customer // row
else:
    column = (customer // row) + 1

# print(row)

for i in range(0, row):
  for j in range(1, column + 1):
    seat = i * column + j
    if seat > customer:
      break
    print(seat, end=" ")
  print()
import calendar
import datetime

calendar.prcal(2024)

calendar.prmonth(2024,12)

print(calendar.weekday(2024,12,11))

days = ['월','화','수','목','금','토','일']

#오늘의 요일
weekday = datetime.date.today().weekday()
print(weekday)
print('오늘은 ' + days[weekday] + '요일')

weekday = datetime.date(2025, 12, 25).weekday()
print('크리스마스는 '+days[weekday]+'요일')
 
#날짜로 요일 알아내기-함수로 정의
def get_weekday(yyyy, mm, dd):
    days = ['월','화','수','목','금','토','일']
    idx = datetime.date(yyyy, mm, dd).weekday()
    print("{}년 {}월 {}일 {}요일".format(yyyy, mm, dd, days[idx]))

get_weekday(2024,12,24)

import time

a = time.time()
print(a)
time.sleep(2)
b = time.time()
print(b-a)

print(time.localtime())
time_str = time.localtime()
print(time_str.tm_year)
print(time.ctime()) #읽기쉬운 str 형태로 시간을 알려 준다.
print(time.ctime(a))
print(time.ctime(b))

#1970.1.1일 기준
year = round(time.time()/(365*24*60*60)) #1년을 초로 바꿈
print(year)
day = round(time.time()/(24*60*60))
print(day)

#수행시간 구하기-코드 시간 얼마나 걸리는지 알기 위해 익히기-> 함수로 정의해서 사용하면 편하다.
def check_time(func):
    start = time.time()
    func()
    end = time.time()
    print(f"수행시간 : {end-start}초")

def a():
    for i in range(10):
        print(i)
        time.sleep(1)

def b():
    for i in range(100):
        print(i)
        time.sleep(0.5)

check_time(a)
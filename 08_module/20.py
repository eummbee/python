import os

os.chdir("C:/Users/user/codingon/python/08_module") #디렉터리 경로
dir = os.popen('git status') #dir 명령으로 열기
print(dir.read()) #디렉터리 보리(읽기)
print(os.listdir()) #파일을 리스트에 저장
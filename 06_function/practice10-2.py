#실습4. 함수 & 스택(리스트)
import sys
line = int(sys.stdin.readline())
stack = []

#명령 함수
def push(X):
    stack.append(X)

def pop():
    if len(stack) != 0:
        d = stack.pop()
        print(d)
    else:
        print(-1)

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stack) ==0:
        print(-1)
    else:
        print(stack[len(stack)-1])


for i in range(line):
    command = sys.stdin.readline().split()
    
    if command[0] == 'push':
        push(command[1])
    elif command[0] == 'pop':
        pop()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    else:
        top()

#match case 사용하기
for i in range(line):
    command = sys.stdin.readline().split()
    
    match command[0]:
        case 'push':
            push(command[1]) 
        case 'pop':
            pop()
        case 'size':
            size()
        case 'empty':
            empty()
        case 'top':
            top()










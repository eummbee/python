import sys
# print(sys.argv)
# args = sys.argv[1:]
# print(args)

# print(int(sys.argv[1]) + int(sys.argv[2]))

#사용자가 입력한 모든 숫자의 합
# a = 0
# for i in sys.argv[1:]:
#     a += int(i)
# print(a)

# print(sum(map(int,sys.argv[1:])))

#세 개를 입력 받는데 mul이면 두 수를 곱하고, add면 두 수를 더해라
# args = list(map(int, sys.argv[2:]))
# if len(sys.argv) != 4:
#     print("error")
# else:
#     if sys.argv[1] == "mul":
#         print(args[0]*args[1])
#     elif sys.argv[1] == "add":
#         print(args[0]+args[1])

#다른 풀이
# args = sys.argv[1:]

# if len(args) != 3:
#     print("error")
#     sys.exit(0) #프로그램 전체를 나가는 것(sys_ex1.py)->else를 쓰지 않아도 에러 처리를 할 수 있다. 
# else:
#     if args[0] == "mul":
#         print(int(args[1])*int(args[2]))
#     elif args[0] == "add":
#         print(int(args[1])+int(args[2]))

args = sys.argv[1:]

if len(args) != 3:
    print("error")
    sys.exit(0) #프로그램 전체를 나가는 것(sys_ex1.py)->else를 쓰지 않아도 에러 처리를 할 수 있다. 

if args[0] == "mul":
    print(int(args[1])*int(args[2]))
elif args[0] == "add":
    print(int(args[1])+int(args[2]))
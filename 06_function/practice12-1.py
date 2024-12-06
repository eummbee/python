#프로그래머스 문제 풀이
def solution():
    for i in range(len(arr)):
        if arr[i] >= 50 and arr[i] % 2 == 0:
            arr[i] = arr[i]/2
        elif arr[i] < 50 and arr[i] % 2 == 1:
            arr[i] = arr[i]*2
        else:
            arr[i] = arr[i]
    print(arr)

arr = list(map(int, input().split()))
solution()


# def solution(arr):
#     answer = []
#     for i in range(len(arr)):
#         if arr[i] >= 50 and arr[i] % 2 == 0:
#             arr[i] = arr[i]/2
#         elif arr[i] < 50 and arr[i] % 2 == 1:
#             arr[i] = arr[i]*2
#         else:
#             arr[i] = arr[i]
#         answer.append(arr[i])
#     return answer

# print(solution([1,2,3,100]))

def solution(myString):
    answer = []
    a = myString.split("x")
    print(a)
    for i in range(len(a)):
        answer.append(len(a[i]))
    return answer
solution("oxooxo")
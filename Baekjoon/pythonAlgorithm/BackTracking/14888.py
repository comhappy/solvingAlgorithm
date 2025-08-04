# 연산자 끼워넣기, 끼워넣어라~

# def cal_result():
#     result = num[0]

#     cal = str(num[0])

#     for i in range(N - 1):
#         if oper_list[i] == 0:    # '+'
#             result += num[i + 1]
#             cal += "+" + str(num[i + 1])
#         elif oper_list[i] == 1:  # '-'
#             result -= num[i + 1]
#             cal += "-" + str(num[i + 1])
#         elif oper_list[i] == 2:  # '*'
#             result *= num[i + 1]
#             cal += "*" + str(num[i + 1])
#         elif oper_list[i] == 3:  # '/'
#             if result < 0 and num[i + 1]:  # 음수 / 양수 인 경우
#                 result *= -1
#                 result //= num[i + 1]
#                 result *= -1

#                 cal += "/" + str(num[i + 1])
#             else:
#                 result //= num[i + 1]
#                 cal += "/" + str(num[i + 1])

#     print(str(cal) + " = " + str(result))

#     return result

def cal_result():
    result = num[0]

    for i in range(N - 1):
        if oper_list[i] == 0:    # '+'
            result += num[i + 1]
        elif oper_list[i] == 1:  # '-'
            result -= num[i + 1]
        elif oper_list[i] == 2:  # '*'
            result *= num[i + 1]
        elif oper_list[i] == 3:  # '/'
            if result < 0 and num[i + 1]:  # 음수 / 양수 인 경우
                result *= -1
                result //= num[i + 1]
                result *= -1
            else:
                result //= num[i + 1]

    return result

def dfs(oper_list): # 연산자를 넣은 index
    if len(oper_list) == (N - 1):   # 연산자를 다 사용한 경우, 계산
        result = cal_result()
        
        global answer
        answer.append(result)

        return False
    else:   # 연산자를 추가
        for i in range(4):
            if oper[i] != 0:
                oper[i] -= 1    # 해당하는 연산자 사용
                oper_list.append(i)

                dfs(oper_list)

                oper[i] += 1
                oper_list.pop()

        return True


N = int(input())

num = list(map(int, input().split()))
oper = list(map(int, input().split()))    # 덧셈, 뺄셈, 곱셈, 나눗셈의 순서
oper_list = list()

answer = []

dfs(oper_list)

print(max(answer))
print(min(answer))
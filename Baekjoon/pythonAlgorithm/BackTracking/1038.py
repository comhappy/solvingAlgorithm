# 감소하는 수

n = int(input())

number = 0
times = 0

while(1):
    # 감소하는 수 검사
    if number > 9876543210: # 최대 감소하는 수인 경우
        number = -1
        break

    str_number = list(map(int, str(number)))
    degree_flag = 0

    for i in range(len(str_number) - 1):
        if str_number[i] <= str_number[i + 1]:  # 감소하는 수가 아닌 경우
            str_number[i] += 1
            str_number[i + 1] = 0

            number = int("".join(map(str, str_number)))
            degree_flag = 1

            break

    # 감소하는 수 여부 확인
    if degree_flag == 0:    # 감소하는 수인 경우
        if times == n:
            break
        else:
            times += 1
            number += 1

print(number)
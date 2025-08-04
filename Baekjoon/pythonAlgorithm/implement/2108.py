# 통계학

import sys
input = sys.stdin.readline

def mean(num): # 평균값
    sum = 0
    length = 0

    for i in num:
        sum += i
        length += 1

    num_mean = round(sum / length)

    if num_mean == -0:
        num_mean = 0

    return num_mean  # 반올림 함수


def middle(num):   # 중앙값
    length = 0

    for _ in num:
        length += 1

    return num[length // 2]


def mode(num): # 최빈값, 최빈값이 여러개인 경우 2번째로 작은 값을 출력
    if len(num) == 1:   # 숫자가 1개인 경우 그대로 return
        return num[0]

    count = [0 for _ in range(len(num))]    # 정렬된 num 배열을 순회하면서 앞뒤로 비교해서 중복되는 숫자의 개수를 저장하는 리스트

    count_index = 0

    for i in range(len(num) - 1):
        if num[i] == num[i + 1]:    # 앞뒤로 같은 경우
            count[count_index] += 1
        else:   # 중복된 숫자가 끊긴 경우 새로운 index를 갱신
            count_index = i + 1

    # num = [1, 1, 2, 2, 3, 3, 3] 일 경우,
    # count=[1, 0, 1, 0, 2, 0, 0] 로 갱신됨. 이후, count에서 최댓값을 가지는 index를 찾고(현재는 4) num[index]를 return
    # 만약 count의 최댓값이 같다면 modelist에 index를 추가해서 두번째 값을 return

    max_count = 0
    modelist = list()

    for i in range(len(count)):
        if count[i] > max_count:    # 최대로 나온 경우, 중복되는 경우도 생각해주어야함.
            modelist.clear()
            modelist.append(i)
            max_count = count[i]
        elif count[i] == max_count:
            modelist.append(i)  # 해당하는 index를 추가

    if len(modelist) == 1:
        return num[modelist[0]]
    else:
        return num[modelist[1]]


def diff(num): # 최댓값과 최솟값의 차이
    max = num[0]
    min = num[0]

    for i in num:
        if max < i:
            max = i
        
        if min > i:
            min = i

    return max - min


N = int(input())
num = list()

for _ in range(N):
    num.append(int(input()))

# 비교를 위한 정렬
num.sort()

print(mean(num))
print(middle(num))
print(mode(num))
print(diff(num))
# 펠린드롬?

import sys
input = sys.stdin.readline

def DP():
    answer = [[0 for _ in range(n)] for _ in range(n)]  # s ~ e 까지 숫자가 팰린드롬인지 확인하는 배열

    # 1개짜리 수는 팰린드롬
    for i in range(n):
        answer[i][i] = 1

    # 팰린드롬이 홀수인 경우
    for i in range(n):  # 중간 수
        for j in range(1, n):   # 양옆에 추가되는 수를 확인
            pre = i - j
            next = i + j

            if pre >= 0 and next < n:    # 범위를 만족하는 경우
                if number[pre] == number[next] and answer[pre + 1][next - 1] == 1:  # 팰린드롬인 경우
                    answer[pre][next] = 1

    # 팰린드롬이 짝수인 경우
    for i in range(n - 1):
        if number[i] == number[i + 1]:  # 두개의 수가 같아야 함
            answer[i][i + 1] = 1

            for j in range(1, n):
                pre = i - j
                next = i + 1 + j

                if pre >= 0 and next < n:    # 범위를 만족하는 경우
                    if number[pre] == number[next] and answer[pre + 1][next - 1] == 1:  # 팰린드롬인 경우
                        answer[pre][next] = 1

    return answer


n = int(input())
number = list(map(int, input().split()))
m = int(input())

answer = DP()

for _ in range(m):
    s, e = map(int, input().split())
    print(answer[s - 1][e - 1])
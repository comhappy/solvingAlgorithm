# 가장 긴 증가하는 부분 수열
# https://4legs-study.tistory.com/106

def DP():
    answer = [1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if A[j] < A[i]:
                answer[i] = max(answer[i], answer[j] + 1)   # 원래값과, 변경되는 값 비교

    print(max(answer))


n = int(input())
A = list(map(int, input().split()))

DP()
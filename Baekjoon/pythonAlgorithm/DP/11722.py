# 가장 긴 감소하는는 부분 수열

def DP():
    answer = [1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if A[j] > A[i]:
                answer[i] = max(answer[i], answer[j] + 1)

    print(max(answer))


n = int(input())
A = list(map(int, input().split()))

DP()
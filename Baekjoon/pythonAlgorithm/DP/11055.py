# 가장 큰 증가하는 부분 수열

def DP():
    answer = [i for i in A]

    for i in range(n):
        for j in range(i):
            if A[j] < A[i]:
                answer[i] = max(answer[i], answer[j] + A[i])

    print(max(answer))


n = int(input())
A = list(map(int, input().split()))

DP()
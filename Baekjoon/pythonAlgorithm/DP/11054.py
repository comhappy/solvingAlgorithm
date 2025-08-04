# 가장 긴 바이토닉 부분 수열

def DP():
    up = [1 for _ in range(n)]
    down = [1 for _ in range(n)]
    result = 0

    for i in range(n):
        for j in range(i):
            if A[j] < A[i]: # 증가하는 부분
                up[i] = max(up[i], up[j] + 1)
    
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i - 1, -1):
            if A[j] < A[i]: # 감소하는 부분
                down[i] = max(down[i], down[j] + 1)
                
    # 정답 구하기    
    for i in range(n):
        result = max(result, up[i] + down[i] - 1)

    print(up)
    print(down)

    print(result)


n = int(input())
A = list(map(int, input().split()))

DP()


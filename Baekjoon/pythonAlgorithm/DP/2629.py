# 양팔저울

a_count = int(input())  # 추의 개수
A = list(map(int, input().split())) # 추의 무게
b_count = int(input())  # 구슬의 개수
B = list(map(int, input().split())) # 구슬의 무게

# dp[i][j]의 의미 : A[i]까지 추를 사용해서 j의 무게를 만들 수 있는지 여부(j는 양 저울의 무게 차이)
dp = [[0 for _ in range(sum(A) + 1)] for _ in range(a_count + 1)]  # (추 전체의 무게)g 구하기

# 기저상태 저장
dp[0][0] = 1

for i in range(a_count):
    dp[i + 1][A[i]] = 1

for i in range(a_count):
    for j in range(sum(A) + 1):
        # 무게를 만들 수 있는 경우
        if dp[i][j] == 1:
            dp[i + 1][j] = 1                # 다음 추를 사용하지 않는 경우
            dp[i + 1][abs(j - A[i])] = 1    # 다음 추를 왼쪽에 놓는 경우
            dp[i + 1][j + A[i]] = 1         # 다음 추를 오른쪽에 놓는 경우

for i in range(b_count):
    if B[i] > sum(A):
        print("N", end=' ')
    elif dp[a_count][B[i]]:
        print("Y", end=' ')
    else:
        print("N", end=' ')
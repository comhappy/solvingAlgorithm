# 공통 부분 문자열

import sys, copy
input = sys.stdin.readline

A = input().strip()
B = input().strip()

len_A = len(A)
len_B = len(B)

save = [0 for _ in range(len_A + 1)]    # 이전 dp 정보를 저장
dp = [0 for _ in range(len_A + 1)]
answer = 0

for i in range(1, len_B + 1):
    for j in range(1, len_A + 1):
        # 끝 문자가 같은 경우, 끝 문자는 같다고 생각하고 값을 결정해줌
        # ex) AB'C'와 BC비교 값 = AB와 B 비교값 + 1
        if B[i - 1] == A[j - 1]:  
            dp[j] = save[j - 1] + 1

        if dp[j] > answer:
            answer = dp[j]

    # 이전 dp 정보 저장, dp 배열 초기화
    save = dp
    dp = [0 for _ in range(len_A + 1)]
        
print(answer)
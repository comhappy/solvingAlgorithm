# N-Queen 문제, BackTracking 유형의 유명한 문제
# 모든 체스판을 DFS 해야하나?

def dfs(queen): # queen은 놓은 말 개수
    global result
    
    if queen == N:  # 정답인 경우
        result += 1

        return False
    else:   # queen을 놓아야 하는 경우
        for i in range(N):
            if not column[i] and not line1[queen + i] and not line2[(N - 1) + queen - i]:
                column[i] = True
                line1[queen + i] = True
                line2[(N - 1) + queen - i] = True

                dfs(queen + 1)

                column[i] = False
                line1[queen + i] = False
                line2[(N - 1) + queen - i] = False


N = int(input())

# 열 점유 여부
column = [False] * N
# y=x 대각선 점유 여부
line1 = [False] * (2 * N - 1)
# y=-x 대각선 점유 여부
line2 = [False] * (2 * N - 1)

result = 0

dfs(0)

print(result)
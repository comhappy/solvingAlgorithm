# 동전 2

def DP():
    answer = [[k + 1 for _ in range(k + 1)] for _ in range(n + 1)]

    # 나머지 DP 테이블 채우기
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if coin[i -1] == j: # 동전을 1개 사용하는 경우
                answer[i][j] = 1
            elif j - coin[i - 1] >= 0:
                x =answer[i][j] # 현재값
                y =answer[i - 1][j] # 이전 동전들의 개수
                z =answer[i][j - coin[i - 1]] + 1   #현재 동전을 1개 사용한 개수 비교
                
                answer[i][j] = min(x, y, z)
            else:
                answer[i][j] = min(answer[i][j], answer[i - 1][j])

    for i in answer:
        print(i)

    if answer[n][k] == k + 1:
        print(-1)
    else:
        print(answer[n][k])


n, k = map(int, input().split())
coin = list()

for i in range(n):
    coin.append(int(input()))

DP()
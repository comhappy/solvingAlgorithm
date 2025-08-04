# 다리놓기
# 다리를 놓을 사이트를 구하고 순서대로 연결해준다.
# 이항계수를 DP를 사용해서 구한다.

import sys
input = sys.stdin.readline


def DP():
    com = [[1 for _ in range(m + 1)] for _ in range(m + 1)]

    com[0][0] = 0

    # DP를 사용한 이항계수 구하기
    for i in range(1, m + 1):
        for j in range(1, i):
            com[i][j] = com[i - 1][j] + com[i - 1][j - 1]

    print(com[m][n])


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())    # 구해야하는것: mCn

    if n == 0 and m == 0:
        print(0)
    elif n == m:
        print(1)
    else:
        DP()
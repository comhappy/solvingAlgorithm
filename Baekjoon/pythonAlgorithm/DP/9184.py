# 신나는 함수 실행

import sys
input = sys.stdin.readline

wabc = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]

# 조건을 통해 범위를 나누어 줌줌
for i in range(1, 21):
    for j in range(1, i + 1):  # b의 범위, a >= b 인 경우
        for k in range(1, 21):  # c의 범위
            wabc[i][j][k] = wabc[i - 1][j][k] + wabc[i - 1][j - 1][k] + wabc[i - 1][j][k - 1] - wabc[i - 1][j - 1][k - 1]

    for j in range(i + 1, 21):  # b의 범위, a < b 인 경우
        for k in range(1, j + 1):   # c의 범위, b >= c 인 경우
            wabc[i][j][k] = wabc[i - 1][j][k] + wabc[i - 1][j - 1][k] + wabc[i - 1][j][k - 1] - wabc[i - 1][j - 1][k - 1]

        for k in range(j + 1, 21):  # c의 범위, b < c 인 경우
            wabc[i][j][k] = wabc[i][j][k - 1] + wabc[i][j - 1][k - 1] - wabc[i][j - 1][k]

# if문을 통한 조건 반별
# for i in range(1, 21):
#     for j in range(1, 21):
#         for k in range(1, 21):
#             if i < j and j < k:
#                 wwabc[i][j][k] = wwabc[i][j][k - 1] + wwabc[i][j - 1][k - 1] - wwabc[i][j - 1][k]
#             else:
#                 wwabc[i][j][k] = wwabc[i - 1][j][k] + wwabc[i - 1][j - 1][k] + wwabc[i - 1][j][k - 1] - wwabc[i - 1][j - 1][k - 1]


while(1):
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break

    if a <= 0 or b <= 0 or c <= 0:
        print("w({}, {}, {}) = {}".format(a, b, c, 1))
    elif a > 20 or b > 20 or c > 20:
        print("w({}, {}, {}) = {}".format(a, b, c, wabc[20][20][20]))
    else:
        print("w({}, {}, {}) = {}".format(a, b, c, wabc[a][b][c]))
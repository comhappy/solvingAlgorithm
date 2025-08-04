# 방 번호

import math

N = input()
numset = [0 for _ in range(10)]

# 숫자의 개수 세기
for i in N:
    if i == "9":
        numset[6] += 1
    else:
        numset[int(i)] += 1

numset[6] = math.ceil(numset[6] / 2)

print(max(numset))
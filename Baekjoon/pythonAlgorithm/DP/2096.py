# 내려가기

import sys, copy
input = sys.stdin.readline

n = int(input())

max_a, max_b, max_c = 0, 0, 0
min_a, min_b, min_c = 0, 0, 0

for _ in range(n):
    a, b, c = map(int, input().split()) # 입력 받는 수

    # Memoization
    max_a += a
    max_b += b
    max_c += c

    min_a += a
    min_b += b
    min_c += c

    # 조건에 맞는 값 설정
    max_a, max_b, max_c = max(max_a, max_b), max(max_a, max_b, max_c), max(max_b, max_c)
    min_a, min_b, min_c = min(min_a, min_b), min(min_a, min_b, min_c), min(min_b, min_c)

print(max(max_a, max_b, max_c), min(min_a, min_b, min_c))
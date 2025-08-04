# 알고리즘 수업 - 피보나치 수 1

n = int(input())

code1 = [1 for _ in range(n + 1)]

for i in range(3, n + 1):
    code1[i] = code1[i - 1] + code1[i - 2]

print(code1[n], n - 2)
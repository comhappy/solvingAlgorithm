# 카드 구매하기

import sys
input = sys.stdin.readline

def DP():
    answer = [i for i in p] # 초기 최대값을 p값으로 설정
    
    for i in range(2, n + 1):
        for j in range(i // 2 + 1): # i를 2로 나눈 몫까지 반복
            answer[i] = max(answer[i], answer[i - j] + p[j])

    print(answer[n])
            

n = int(input())
p = [0]

for i in list(map(int, input().split())):
    p.append(i)

DP()
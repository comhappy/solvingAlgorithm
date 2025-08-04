# 신기한 소수 찾기
# DFS를 사용하여 자릿수 탐색

import sys

sys.setrecursionlimit(10000)    # 백준 온라인 저지의 기본 recursionlimit은 1000이므로 설정을 해주어야함

N = int(sys.stdin.readline())   

# 소수를 판별
def isPrime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
        
    return True

def dfs(num): # num은 해당하는 숫자
    if len(str(num)) == N:   # num의 길이가 구하고자하는 자릿수인 경우 숫자를 출력
        print(num)
    else:   # 해당 숫자가 소수인지 판별
        for i in range(1, 10, 2):   #홀수에 대해서 판별
            if isPrime(num * 10 + i):   # 해당 숫자가 소수인 경우만 dfs 확장, 아니면 확장하지 않음(가지치기)
                dfs(num * 10 + i)


dfs(2)
dfs(3)
dfs(5)
dfs(7)